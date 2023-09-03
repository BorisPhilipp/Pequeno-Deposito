#4) Escreva uma função que converte um número decimal em sua representação binária
#usando uma pilha.
#===================================================================================

def Binario(num):
    bin = ""
    if num == 0:
        return "0" 
    
    while num > 0:
        modulo = num % 2
        num = num // 2
        bin = str(modulo) + bin
    return bin

digit = int(input("Digite um Número Inteiro para converter em Binario: "))
print(Binario(digit))
