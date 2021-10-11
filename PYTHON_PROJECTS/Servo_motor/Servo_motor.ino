const int Servo_Motor = 2;

void setup() {
  Serial.begin(9600);
  pinMode(Servo_Motor, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()>0)
  {
    int angle = Serial.parseInt();
    if(Serial.read()== '\n')
    {
      angle = constrain(angle, 0, 200);
      analogWrite(Servo_Motor, angle);
      }
    }

}
