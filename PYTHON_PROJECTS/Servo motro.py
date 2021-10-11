import serial
#from serial import Serial
import cv2
import math
import cvzone
from cvzone.HandTrackingModule import HandDetector

serialcomm = serial.Serial('COM18',9600)
serialcoomm.timeout = 1
cap=cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=1)
I=[]
while True:
    success,img = cap.read()
    img = cv2.resize (img,(300,250))
    img =detector.findHands(img)
    I, box = detector.findPosition(img)
    if I:
        f = detector.fingersUp()
        x1 = I[4][0]
        x2 = I[4][1]
        y1 = I[8][0]
        y2 = I[8][1]
        cv2.circle(img(x1,y1),7,(0,255,255),2)
        cv2.circle(img(x2,y2),7,(0,255,255),2)
        cv2.circle(img(x1,y1),(x2,y2),(0,0,255),2)
        d = int(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)*1.0))
        d = int((d/120)*255)
        d1 = int((d/200)*90)

        cv2.putText(img,"Angle:-",(20,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)

        e='\n'
        serialcomm.write(str(d).encode())
        serialcomm.write(e.encode())

    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
