#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);


void setup() {
Serial.begin(9600);
lcd.init();
lcd.backlight();
lcd.begin(16,2);
lcd.setCursor(3,0);
lcd.print("Bem-Vindo");
lcd.setCursor(0,1);
lcd.print(".");
delay(1000);
lcd.setCursor(1,1);
lcd.print(".");
delay(1000);
lcd.setCursor(2,1);
lcd.print(".");
delay(1000);
lcd.setCursor(3,1);
lcd.print(".");
delay(1000);
lcd.setCursor(4,1);
lcd.print(".");
delay(1000);
lcd.setCursor(5,1);
lcd.print(".");
delay(1000);
lcd.clear();
  

}

void loop() {
  

}
