#define trigger 7
#define echo 8

int dist = 0;

int red = 6;
int yellow = 5;
int green = 4;


void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  
  Serial.begin(9600);

  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);

}

void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo,HIGH);
  dist = dist / 58;
  
  Serial.println("Distancia: "+ String(dist));
  

  if(dist < 50){
    digitalWrite(red,HIGH);
    digitalWrite(yellow,LOW);
    digitalWrite(green,LOW);

  }else if (dist < 100){
    digitalWrite(red,LOW);
    digitalWrite(yellow,HIGH);
    digitalWrite(green,LOW);

  }else{
    digitalWrite(red,LOW);
    digitalWrite(yellow,LOW);
    digitalWrite(green,HIGH);

  }
}