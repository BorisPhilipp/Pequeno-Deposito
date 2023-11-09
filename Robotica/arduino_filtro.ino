#include <Ultrasonic.h>
Ultrasonic ultrassom(2,3);

long distancia;

void setup() {
Serial.begin(9600);
pinMode(7, OUTPUT);
}

void loop() {
distancia = ultrassom.read(CM);
Serial.print(distancia);
Serial.println("cm");
delay(100);

if (distancia >= 15 && distancia <= 20){
tone(7, 85);
delay(1000);
noTone(7);
}
}
