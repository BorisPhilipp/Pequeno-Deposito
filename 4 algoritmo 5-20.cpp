//4) Escreva um algoritmo que leia um valor verifique se ele se encontra no intervalo entre 5 e 20.

#include<iostream>
using namespace std;
int main(){
    int num;

    cout<<"Informe um numero"<<endl;
    cin>>num;

    cout<<boolalpha;
    bool numinter{false};
    numinter = (num >5) && (num<20);
    cout<<"O valor "<<num<<" esta dentro do intervalo entre 5 - 20? "<<numinter<<endl;

    return 0;
}









