//14)Faça um algoritmo que leia as 3 notas de um aluno e calcule a sua média
//anual ponderada, com o peso: 2, 3 e 5, respectivamente. Se a nota obtida for
//entre 6 a 10 está aprovado; se é entre 4 e 5.9 em recuperação, se é menor
//que 4 reprovado. Se o aluno está em recuperação ler a nota de recuperação
//e calcular a média final (que é a média entre a média anual e a nota de
//recuperação). Se a média final é menor que 5 o aluno está reprovado após
//recuperação, se é igual ou maior que 5 está aprovado após recuperação.

#include<iostream>
using namespace std;
int main(){
    float nota1, nota2, nota3, media, media_final, recup;

    cout<<"Digite a Primeira Nota"<<endl;
    cin>>nota1;

    cout<<"Digite a Segunda Nota"<<endl;
    cin>>nota2;

    cout<<"Digite a Terceira Nota"<<endl;
    cin>>nota3;

    media = (2*nota1 + 3*nota2 + 5*nota3)/10;

    if(media>=6){
        cout<<"Esta Aprovado!"<<endl;
    } else if (media>=4 && media<5.9){
        cout<<"Esta em Recuperacao : "<<media<<endl;
        cout<<"Digite a Nota da Recuperacao: "<<endl;
        cin>>recup;
        media_final = (media + recup)/2;

        if(media_final>=5){
            cout<<"APROVADO APOS RECUPERACAO!!!!!!!!"<<endl;
        } else {
            cout<<"REPROVADO APOS RECUPERACAO"<<endl;
        } 
    } else {
        cout<<"REPROVADO"<<endl;

}
}