//6) Ler um número inteiro que representa um dia da semana a apresentar o nome do dia correspondente (domingo, segunda-feira, ...).

#include<iostream>
using namespace std;
int main(){
int dia;

cout<<"Insira um numero de 1 - 7 (Cada numero representa um dia da semana)"<<endl;
cin>>dia;

switch (dia){
    case 1:
    cout<<"Segunda-Feira!";
    break;
    
    case 2:
    cout<<"Terça-Feira!";
    break;
    
    case 3:
    cout<<"Quarta-Feira!";
    break;
    
    case 4:
    cout<<"Quinta-Feira!";
    break;
    
    case 5:
    cout<<"Sexta-Feira!";
    break;
    
    case 6:
    cout<<"Sabado!";
    break;
    
    case 7:
    cout<<"Domingo!";
    break;
    
    default:
    cout<<"Numero Invalido";
}
}
