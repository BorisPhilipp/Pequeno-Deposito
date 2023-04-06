//7) Ler dois valores inteiros e apresentar a adição destes valores, quando o
//primeiro valor for maior que o segundo, caso contrário, efetuar a multiplicação dos valores.


#include<iostream>
using namespace std;
int main(){
    
    int valor1{0}, valor2{0};
    cout<<"Digite o Primeiro Valor"<<endl;
    cin>>valor1;

    cout<<"Digite o Segundo Valor"<<endl;
    cin>>valor2;

   if (valor1>valor2){
   cout<<"O resultado e: "<<valor1+valor2;
    }
   
    else {
        cout<<"O resultado e: "<<valor2*valor1;
    }
}

