/*
8) Fazer um programa em "C++" que solicite 2 números e informe:

a) A soma dos números;
b) O produto do primeiro número pelo quadrado do segundo;
c) O quadrado do primeiro número;
d) A raiz quadrada da soma dos quadrados;
e) O módulo do primeiro número.
*/

#include<iostream>
#include<cmath>
using namespace std;
int main(){
double valorsoma, raiz;
int valor1, valor2;


    cout<<"Insira o Primeiro Valor"<<endl;
    cin>>valor1;
    cout<<"Insira o Segundo Valor"<<endl;
    cin>>valor2;
    valorsoma = valor1 * (valor2 * valor2);
    raiz = sqrt(pow(valor1,2)+pow(valor2,2));


    cout<<"==================================================="<<endl;
    cout<<"A Soma dos dois valores e : "<<valor1+valor2<<endl;
    cout<<"O produto do primeiro numero ("<<valor1<<") pelo quadrado do segundo numero ("<<valor2<<") e: "<<valorsoma<<endl;
    cout<<"O quadrado do primeiro numero e: "<<valor1 * valor1<<endl;
    cout<<"A raiz quadrada da soma dos quadrados e: "<<raiz<<endl;
    cout<<"O modulo do primeiro numero e: "<<valor1%2<<endl;
}