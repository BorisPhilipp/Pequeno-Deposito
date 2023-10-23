def primeiraFuncao():   #assinatura da funcao
    print("Minha primeira função.")

primeiraFuncao()

#Parâmetros
def imprimeNome(nome):
    print(f'Nome: {nome}')

imprimeNome("João")
imprimeNome("Maria")
imprimeNome("Pedro")

def monta_computador(cpu, armazenamento, memoria):
    print(f"A configuração é: \n\t - CPU: {cpu} \n\t - Armazenamento: {armazenamento}TB \n\t - Memória: {memoria}GB")

monta_computador("AMD Ryzen 5 5500U", 1, 8)

#PROCEDIMENTO -> Função Sem Retorno
#FUNÇÃO -> RETORNO

def somaDoisValores(valor1, valor2):
    soma = valor1 + valor2
    return soma

resultado = somaDoisValores(5,9)
print("O valor da soma é: ", resultado)
print("O valor da soma é: ", somaDoisValores(15,20))

'''
- Escreva uma função que recebe
como entrada um número inteiro positivo n 
e retorne a soma de todos os inteiros positivos menores ou iguais a n.
'''

def somaDiferente(numPositivo):
    for i in range(numPositivo+1):
        print(i)

numeroUser = somaDiferente(int(input("Digite um Numero Positivo: ")))

