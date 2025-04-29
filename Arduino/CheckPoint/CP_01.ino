#define ledGreen 13
#define ledYellow 12
#define ledRed 11
#define buzzer 2
#define ldr A0
float ldrValor = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  pinMode(ledRed, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(ldr, INPUT);

}

void loop() {
  lrdValor = analogRead(ldr);

  Serial.print(ldrValor);

  if(ldrValor < 200){
    digitalWrite(ledGreen, HIGH);
    digitalWrite(ledYellow, LOW);
    digitalWrite(ledRed, LOW);
  }else if(ldrValor < 400){
    digitalWrite(ledYellow, HIGH);
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledRed, LOW);
    digitalWrite(buzzer, HIGH);
    delay(3000);
    digitalWrite(buzzer,LOW);
  }else{
    digitalWrite(ledYellow, LOW);
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledRed, HIGH);
  }

}