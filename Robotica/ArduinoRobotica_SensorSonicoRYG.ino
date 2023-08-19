#include <Ultrasonic.h> //Incluindo a biblioteca do ultrasonic
//trigger 12
//echo 13
// vcc 5v
//gnd gnd
Ultrasonic ultrasonic(12, 13);  //trigger,echo 
int distancia;
const int pinLEDR = 2;                              //define o nome do led e sua posição
const int pinLEDY = 3;
const int pinLEDG = 4;


void setup() {
                                                    // put your setup code here, to run once:
Serial.begin(9600); 
pinMode(pinLEDR, OUTPUT);                         //define que tipo informação será transmitida, INPUT = receber, OUTPUT = saida
pinMode(pinLEDY, OUTPUT);
pinMode(pinLEDG, OUTPUT);

}

void loop() {
                                                    // put your main code here, to run repeatedly:
distancia = ultrasonic.read();                      //variavel usada pra calcular distancia em centímetros
Serial.print ("Distancia em CM: ");
Serial.println (distancia);
if(distancia >= 0 && distancia <= 9){
digitalWrite(pinLEDR, HIGH);
digitalWrite(pinLEDY, LOW);
digitalWrite(pinLEDG, LOW);
} else if(distancia >= 10 && distancia <= 19){
  digitalWrite(pinLEDY, HIGH);
  digitalWrite(pinLEDR, LOW);
  digitalWrite(pinLEDG, LOW);
}else if(distancia > 20) {
    digitalWrite(pinLEDR, LOW);
    digitalWrite(pinLEDY, LOW);
    digitalWrite(pinLEDG, HIGH);
}else{
  digitalWrite(pinLEDY, LOW);
  digitalWrite(pinLEDR, LOW);
  digitalWrite(pinLEDG, LOW);
}
}