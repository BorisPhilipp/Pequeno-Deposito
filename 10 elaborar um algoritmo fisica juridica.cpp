//10)Elaborar um algoritmo que leia uma letra que pode ser ‘F’ ou ‘J’ e mostra a
//mensagem “pessoa física”, “pessoa jurídica” ou "tipo de pessoa inválido",conforme o caso.

#include<iostream>
using namespace std;
int main(){
    char pessoas{};
    cout<<"F ou J"<<endl;
    cin>>pessoas;

    switch(pessoas){
        case'f':
        case'F':
        cout<<"Pessoa Fisica"<<endl;
        break;

        case'j':
        case'J':
        cout<<"Pessoa Juridica"<<endl;
        break;

        default:
        cout<<"Tipo de Pessoa Invalido"<<endl;
        break;
    }










}