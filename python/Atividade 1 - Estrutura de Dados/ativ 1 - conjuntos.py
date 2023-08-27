'''#Conjunto
#1) Crie um conjunto com os números de 1 a 10 e imprima o conjunto.
conjunto1 = {1,2,3,4,5,6,7,8,9,10}
print(conjunto1)

=========================================================================================

#2)Crie dois conjuntos, um com os números de 1 a 5 e outro com os números de
#3 a 7. Imprima a união, a interseção e a diferença simétrica dos conjuntos.
conjunto1 = {1,2,3,4,5}
conjunto2 = {3,4,5,6,7}

uniao = conjunto1.union(conjunto2)
print(f"Uniao: {uniao}")

interseccao = conjunto1.intersection(conjunto2)
print(f"Interseccao: {interseccao}")

diferenca = conjunto1.difference(conjunto2)
print(f"Diferença: {diferenca}")

=========================================================================================

#3)Crie um conjunto com as vogais (a, e, i, o, u) e peça ao usuário para digitar
#uma palavra. Imprima as vogais que aparecem na palavra digitada.
vogais = {'a','e','i','o','u'}
digit = input("Digite alguma palavra: ")
for i in digit:
    if i in vogais:
        print(i)

=========================================================================================        

#4)Crie dois conjuntos com nomes de frutas e verifique se há alguma fruta em
#comum entre os conjuntos.
frutas1 = {'abacate','uva','laranja'}
frutas2 = {'caju','melancia','laranja'}
for i in frutas1:
    if i in frutas2:
        print("Existe uma fruta em comum")

=========================================================================================        

#5)Crie um conjunto com números inteiros aleatórios e imprima o maior e o
#menor número do conjunto.
conjunto = {1,2,5,7,12,19}
print(f"Numero Maior: {max(conjunto)}")
print(f"Numero Menor: {min(conjunto)}")

=========================================================================================

#6)Crie um conjunto com as cores do arco-íris (vermelho, laranja, amarelo, verde,
#azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
#digitada está no conjunto e imprima uma mensagem correspondente.

arcoiris = {'vermelho', 'laranja', 'amarelo', 'verde','azul', 'anil', 'violeta'}
pedircor = input("Digite um cor: ")
if pedircor in arcoiris:
    #print(pedircor)

=========================================================================================    

#7)Crie um conjunto com os dias da semana (segunda, terça, quarta, quinta,
#sexta, sábado, domingo) e remova os dias úteis (segunda a sexta). Imprima o
#conjunto resultante.
semana = {'segunda','terca','quarta','quinta','sexta','sábado','domingo'}
semana2 = {'sábado','domingo'}
semana2.difference(semana)
print(semana2)

=========================================================================================

#8)Crie um conjunto com os números de 1 a 20 e outro conjunto com os
#números pares de 1 a 10. Imprima a diferença entre os dois conjuntos.
numeros = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
pares = {0, 2, 4, 6, 8, 10}
diferenca = numeros.difference(pares)

print("A diferença entre os conjuntos é:", diferenca)

=========================================================================================

#9)Crie um conjunto com as notas de um aluno em uma disciplina e verifique se
#ele foi aprovado (média 7) ou reprovado (média abaixo de 7).
notas = {8,9,6,8}
media = sum(notas)/len(notas)

print("Média:")
if media > 7:
    print("Aprovado!")
    print("{:.2f}".format(media))
elif media < 7:
    print("Reprovado!")    

=========================================================================================

#10)Crie um conjunto com os números primos de 1 a 20 e verifique se um número
#digitado pelo usuário está no conjunto.
numPrimos = {2, 3, 5, 7, 11, 13, 17, 19}
digitado = int(input("Digite um número: "))
if digitado in numPrimos:
    print("Seu número ESTÁ no Conjunto")
else:
    print("Seu número NÃO está no conjunto")    
'''