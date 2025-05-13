#include<DHT.h>
#include <LiquidCrystal_I2C.h>

#define dhtpin 2
#define ldrpin A1

DHT dht(dhtpin, DHT22);
LiquidCrystal_I2C lcd(0x27, 16, 2);


void setup() {
  Serial.begin(9600);
  dht.begin();
  lcd.begin(16,2);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(3,0);
  lcd.print("Bem-Vindo");
  lcd.setCursor(0,1);
  lcd.print("Vinheria Agnelo");
  delay(3000);
  lcd.clear();

}

void loop() {
  int temp = dht.readTemperature();
  int umi = dht.readHumidity();
  int lumi = analogRead(ldrpin);

  if(temp < 20){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Temp: ");
    lcd.setCursor(6,0);
    lcd.print(temp);
    lcd.setCursor(0,1);
    lcd.print("Temperatura OK");
    delay(3000);
  }else if(temp<40){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Temp: ");
    lcd.setCursor(6,0);
    lcd.print(temp);
    lcd.setCursor(0,1);
    lcd.print("Alerta");
    delay(3000);
  }else if(temp>=40){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Temp: ");
    lcd.setCursor(6,0);
    lcd.print(temp);
    lcd.setCursor(0,1);
    lcd.print("Perigo");
    delay(3000);    
  }

  if(umi < 20){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Umi: ");
    lcd.setCursor(6,0);
    lcd.print(umi);
    lcd.setCursor(0,1);
    lcd.print("Umidade OK");
    delay(3000);
  }else if(umi<40){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Umi: ");
    lcd.setCursor(6,0);
    lcd.print(umi);
    lcd.setCursor(0,1);
    lcd.print("Alerta");
    delay(3000);
  }else if(umi>=40){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Umi: ");
    lcd.setCursor(6,0);
    lcd.print(umi);
    lcd.setCursor(0,1);
    lcd.print("Perigo");
    delay(3000);    
  }

  if(lumi < 20){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Lumi: ");
    lcd.setCursor(6,0);
    lcd.print(lumi);
    lcd.setCursor(0,1);
    lcd.print("Lumino OK");
    delay(3000);
  }else if(lumi<40){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Lumi: ");
    lcd.setCursor(6,0);
    lcd.print(lumi);
    lcd.setCursor(0,1);
    lcd.print("Alerta");
    delay(3000);
  }else if(lumi>=40){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Lumi: ");
    lcd.setCursor(6,0);
    lcd.print(lumi);
    lcd.setCursor(0,1);
    lcd.print("Perigo");
    delay(3000);    
  }
}