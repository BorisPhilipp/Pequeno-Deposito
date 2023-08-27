'''
#1)Crie uma tupla com os números de 1 a 5 e imprima a tupla.
tupla = (1, 2, 3, 4, 5)
print(tupla)

=========================================================================================

#2)Crie uma tupla com os nomes de três países e imprima o segundo elemento
#da tupla.
tuplaB = ('Alemanha', 'Angola', 'Brasil')
print(tuplaB[1])

=========================================================================================

#3)Crie uma tupla com os valores de uma conta de restaurante (valor da
#refeição, taxa de serviço e valor total). Imprima a tupla.
tuplaC = (50, 10, 60)
print(f"CONTA DE RESTAURANTE - Refeição: R${tuplaC[0]}, Valor da Taxa de Serviço: R${tuplaC[1]}, Valor Total: R${tuplaC[2]}.")

=========================================================================================

#4)Crie uma tupla com os nomes de cinco pessoas e peça ao usuário para
#digitar um número entre 1 e 5. Imprima o nome correspondente ao número
#digitado.
tuplaD = ("Johnny Cage", "Mileena", "Sub-Zero", "Scorpion", "Liu-Kang")
digitadoD = int(input("Digite um número de 1 a 5: "))
print(f"O numero {digitadoD} corresponde com o Nome: {tuplaD[digitadoD]}")

=========================================================================================

#5)Crie uma tupla com as notas de um aluno em uma disciplina e imprima a média das notas.
tuplaE = (6,7,8)
media = sum(tuplaE)/len(tuplaE)
print("A média da nota é: {:.2f}".format(media))

=========================================================================================

#6)Crie uma tupla com as cores do arco-íris (vermelho, laranja, amarelo, verde,
#azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
#digitada está na tupla e imprima uma mensagem correspondente.
tuplaF = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta")
print("Vermelho, Laranja, Amarelo, Verde, Azul, Anil, Violeta")
digit = input("Digite uma das cores acima: ")
if digit in tuplaF:
    print("A Cor está na Tupla.     ele ta sem zap.")
else:
    print("NÃO está na Tupla.")

=========================================================================================
  
#7)Crie uma tupla com as temperaturas de uma semana (sete dias) e imprima a
#temperatura máxima e mínima da semana.
tuplaG = (16, 17, 19, 21, 23, 26, 29)
print(f"A Temperatua mais baixa da semana é {min(tuplaG)} e a mais alta é {max(tuplaG)}")

=========================================================================================

#8)Crie uma tupla com os nomes de cinco frutas e suas respectivas cores.
#Imprima o nome de cada fruta seguido de sua cor.
tuplaH = ("Abacate", "Abacaxi", "Maça", "Laranja", "Uva")
tuplaI = ("Verde", "Amarelo", "Vermelho", "Laranja", "Roxo")
for i in range(len(tuplaH)):
    print(f"{tuplaH[i]} - {tuplaI[i]}")

=========================================================================================

#9)Crie uma tupla com os números de 1 a 10 e outra tupla com os números de 5
#a 15. Imprima a interseção entre as duas tuplas.
tuplaJ = (1,2,3,4,5,6,7,8,9,10)
tuplaK = (5,6,7,8,9,10,11,12,13,14,15)

interseccao = list(set(tuplaJ).intersection(set(tuplaK)))
print(interseccao)

=========================================================================================

#10)Crie uma tupla com as letras do alfabeto e uma segunda tupla com as vogais.
#Imprima a diferença entre as duas tuplas.
tuplaL = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
tuplaM = ('a','e','i','o','u')
diferenca = list(set(tuplaL).difference(set(tuplaM)))
print(f"A diferença é {diferenca}")

=========================================================================================
'''