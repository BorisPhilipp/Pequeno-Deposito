#3)Escreva uma função que use uma pilha para inverter uma string.
#===================================================================================

palavraInput = str(input("Digite uma palavra para inverter: ")).replace(" ", "").lower()
def inverter(palavra):
    Pilha = []
    PilhaInverter = []
    PalavraInverter = ""
    
    for i in range(len(palavra)):
       Pilha.append(palavra[i])
    
    for j in range(len(Pilha)):
        PilhaInverter.append(Pilha.pop())
    
    for i in range(len(PilhaInverter)):
        PalavraInverter += PilhaInverter[i]

    return PalavraInverter
    
print(inverter(palavraInput)) 

