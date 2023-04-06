//13) Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem:
//‘São múltiplos’ ou ‘Não são múltiplos’.

#include<iostream>
using namespace std;
int main(){
    int a, b;

    cout<<"Digite o valor de a"<<endl;
    cin>>a;
    cout<<"Digite o valor de b"<<endl;
    cin>>b;

    if(a % b == 0 || b % a == 0 ){
        cout<<"Sao multiplos"<<endl;
    } else {
        cout<<"Nao sao multiplos"<<endl;
    }
}
