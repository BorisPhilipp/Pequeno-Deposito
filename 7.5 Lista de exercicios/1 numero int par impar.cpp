/*1) Ler um valor inteiro e informar, através de uma mensagem, se este valor é
um número par ou ímpar.
*/

#include<iostream>
using namespace std;
int main(){
    int num;
    cout<<"Digite um Numero: ";
    cin>>num;

    if(num % 2 == 0){
        cout<<num<<" seu numero e par"<<endl;
    } else {
        cout<<num<<" seu numero e impar"<<endl;
    }
    return 0;
}