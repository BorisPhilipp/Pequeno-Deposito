#include <Ultrasonic.h>
Ultrasonic ultrassom(2,3);
int rele = 5;
long distancia;

void setup() {
Serial.begin(9600);
pinMode(7, OUTPUT);
pinMode(rele, OUTPUT);
}

void loop() {
digitalWrite(rele, LOW);
distancia = ultrassom.read(CM);

if (distancia < 20){
digitalWrite(rele, HIGH);
buzzerTocar();
}
}

void buzzerTocar(){
  tone(7, 2500, 100);
  delay(100);
  tone(7, 2500, 100);
  delay(100);
  tone(7, 2500, 100);
  noTone(7);

}