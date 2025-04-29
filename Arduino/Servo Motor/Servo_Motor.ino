#include <Servo.h>
#define servoPin 9

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
 

}

void loop() {
  myServo.write(90);
  delay(500);
  myServo.write(180);
  delay(500);
  myServo.write(0);
  delay(500);

}