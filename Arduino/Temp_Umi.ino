#include<DHT.h>

#define dhtPin 2
#define dhttype DHT11

DHT dht(dhtPin, dhttype);

#define red 3
#define yellow 4
#define green 5


void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);

}

void loop() {
  int temp = dht.readTemperature();
  int umi = dht.readHumidity();

  Serial.println("Temperatura: " + String(temp));
  Serial.println("Umidade: " + String(umi));
  delay(2000);

  if (temp == 27 && umi == 6){
    digitalWrite(red,HIGH);
    digitalWrite(yellow,LOW);
    digitalWrite(green,LOW);
    }
  else if (temp == 27 && umi < 20){
    digitalWrite(red,LOW);
    digitalWrite(yellow,LOW);
    digitalWrite(green,HIGH);
  }
  else {
    digitalWrite(red,LOW);
    digitalWrite(yellow,HIGH);
    digitalWrite(green,LOW);
    }
  

}