#include <Servo.h>
#define servoPin 9
#define ledRed 4
#define ledGreen 3
#define echo 8
#define trigger 7

int dist = 0;

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);

  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);

  pinMode(ledRed,OUTPUT);
  pinMode(ledGreen,OUTPUT);
 

}

void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo,HIGH);
  dist = dist / 58;

  Serial.println("Distancia: "+ String(dist));

  if(dist < 100){
    digitalWrite(ledGreen, HIGH);
    digitalWrite(ledRed, LOW);
    myServo.write(180);
  }  else{
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledRed, HIGH);
    myServo.write(0);
  }
}