//12) Elaborar um algoritmo que lê um valor que se refere a altura de uma pessoa
//e mostra uma mensagem conforme a faixa de altura:
//MENOS QUE 1,50 = "ABAIXO DE UM METRO E MEIO"
//DE 1,50 A 1,80 = "ENTRE UM METRO E MEIO E UM METRO E OITENTA CENTIMETROS"
//MAIS QUE 1,80 = "ACIMA DE UM METRO E OITENTA CENTIMETROS"

#include<iostream>
using namespace std;
int main(){
double altura;

cout<<"Informe sua Altura (X.XX)"<<endl;
cin>>altura;

if(altura<1.50){
    cout<<"Abaixo de Um Metro e Meio"<<endl;
}

if(altura>1.50 && altura<1.80){
    cout<<"Entre Um Metro e Meio e Um Metro e Oitenta Centimetros"<<endl;
}

if(altura>1.80){
    cout<<"Acima de Um Metro e Oitenta Centimetros"<<endl;
}
}
