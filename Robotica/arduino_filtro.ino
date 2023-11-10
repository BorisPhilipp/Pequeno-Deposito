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
Serial.print(distancia);
Serial.println("cm");
delay(250);

if (distancia >= 15 && distancia <= 20){
tone(7, 85);
digitalWrite(rele, HIGH);
delay(1000);
noTone(7);
}
}
