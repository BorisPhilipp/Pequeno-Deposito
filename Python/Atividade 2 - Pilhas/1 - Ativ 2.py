#1) Escreva uma função recursiva em Python que calcule a soma dos primeiros N números inteiros positivos.
#===================================================================================

n = int(input("Digite um Número: "))
def somasN(n):
    if n == 1:
        return 1
    pilha = [n]
    return n + somasN(n - 1)   
resultado = somasN(n)
print(f"O resultado da soma do primeiros numeros é: ", resultado)
