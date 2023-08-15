def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)
print(fatorial(99))

#Somar - Recursivo
def somar(numero):
    #caso base
    if numero == 1:
        return 1
    #chamada recursiva
    return numero  + somar(numero - 1)

x = int(input("Informe um valor: "))
print("Soma: ", somar(x))

#Fibonacci Recursivo
def fibonacci(posicao):
    if posicao == 0:
        return 0
    elif posicao == 1:
        return 1
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)
