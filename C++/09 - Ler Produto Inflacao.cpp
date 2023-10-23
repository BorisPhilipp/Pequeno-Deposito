//9) Fazer um programa em "C++" que lê o preço de um produto e inflaciona esse
//preço em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100.

#include<iostream>
using namespace std;
int main(){
    double preco;

    cout<<"Digite o preco do produto"<<endl;
    cin>>preco;

    if (preco<100){
        preco += preco * 0.1;
            cout<<"O preco do produto inflacionado e: R$ "<<preco<<endl;
    } else {
        preco += preco * 0.2;
            cout<<"O preco do produto inflacionado e: R$ "<<preco<<endl;
    }
}







