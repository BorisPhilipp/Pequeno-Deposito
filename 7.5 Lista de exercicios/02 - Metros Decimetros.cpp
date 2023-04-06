/*2) Fazer um programa em C++ que pergunta um valor em metros e imprime o
correspondente em decímetros, centímetros e milímetros.
*/
#include<iostream>
using namespace std;
int main(){
    double metros, decimetros, centimetros, milimetros;

  cout << "Digite um valor em Metros: ";
  cin >> metros;

  decimetros = metros * 10;
  centimetros = metros * 100;
  milimetros = metros * 1000;

  cout << metros << " Metros equivalem a:" << endl;
  cout << decimetros << " Decimetros" << endl;
  cout << centimetros << " Centimetros" << endl;
  cout << milimetros << " Milimetros" << endl;

  return 0;
}






















