/*3) Fazer um programa em C++ que imprime uma tabela com a tabuada de 1 a 9
*/

#include<iostream>
using namespace std;

int main(){
    int contador{1};

    cout<<"TABUADA"<<endl;
    for (int i = 1; i <= 11 && contador <= 9; i++){
        cout<<contador<<" x "<<i<<" = "<<contador*i<<endl;

        if (i == 10 && contador <= 9){
            cout<<'\n';
            i = 0;
            contador++;
        }
    }
}











