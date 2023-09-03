#2)Escreva uma função recursiva para calcular o número fatorial de um número inteiro positivo.
#===================================================================================

digit = int(input("Digite um Número Inteiro: "))
def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num - 1)
print(f"O Fatorial de {digit} é",fatorial(digit))


