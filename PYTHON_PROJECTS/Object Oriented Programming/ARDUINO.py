import serial
import time

serialcomm = serial.Serial('COM18',9600)
serialcomm.timeout =1

