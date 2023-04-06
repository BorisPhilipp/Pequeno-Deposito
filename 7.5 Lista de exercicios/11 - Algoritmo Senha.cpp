//11)Elabore um algoritmo que lê um número que representa uma senha, verifica
//se a senha está correta ou não, comparando-a com a senha 34567, e informa
//"Acesso autorizado" ou "Acesso negado", conforme o caso.

#include<iostream>
using namespace std;
int main(){
    int senha;
    cout<<"Digite sua Senha"<<endl;
    cin>>senha;

    if(senha ==34567){
        cout<<"Acesso Autorizado"<<endl;
    }
    else{
        cout<<"Acesso Negado"<<endl;
    }
    }
