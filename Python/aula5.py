'''Conjuntos

#Criando um Conjunto vazio:
meu_conjunto = set()
meu_conjunto2 = {1,2,3,4}

meu_conjunto2.add(8)
meu_conjunto2.remove(2)

#Verificar se um elemento esta no conjunto
if 3 in meu_conjunto2:
    print("O conjunto contém o elemento 3")

#Operações
#União
conjunto1 = {1,2,3}
conjunto2 = {9,10,11}
uniao = conjunto1.union(conjunto2)
#print(uniao)

#Intersecção
interseccao = conjunto1.intersection(conjunto2)
#print(interseccao)

#Diferença
diferenca = conjunto1.difference(conjunto2)
#print(diferenca)


#Dicionarios
meu_dicionario = {}
meu_dicionario2 = {'nome':'João','idade':30,'cidade':'Guarapuava'}

#Adicionar elementos
meu_dicionario2['profissão'] = 'programador'

#Remover elementos
del meu_dicionario2['cidade']

#Verificar a existencia de uma chave
if 'idade' in meu_dicionario2:
    print("A chave 'idade' existe no dicionario")

chaves = meu_dicionario2.keys()
valores = meu_dicionario2.values()

#Percorrer um dicionario
for chave,valor in meu_dicionario2.items():
    print(chave,valor)

#Mesclar dois dicionarios
meu_dicionario3 = {'sobrenome':'Silva', 'telefone':123456}
meu_dicionario2.update(meu_dicionario3)
print(meu_dicionario2)


#Tuplas
minha_tupla = ()
minha_tupla2 = (1,2,3,'quatro','cinco',6.0)
#print(minha_tupla2[0])

#Concatenar Tuplas
minha_tupla3 = ('a','b','c')
nova_tupla = minha_tupla2 + minha_tupla3
#print(nova_tupla)

#Verificar a existencia de um valor na tupla
#if 'quatro' in minha_tupla2:
#   print("O elemento 'quatro' existe na tupla")

#Percorrer a tupla
#for elemento in minha_tupla2:
#    print(elemento)
'''

#Desafios
'''
1.Crie um conjunto com os números de 1 a 10 e imprima o conjunto
2.Crie um dicionario vazio e adicione duas chaves e valores a ele
3.Crie uma tupla com os numeros de 1 a 5 e imprima a tupla.
'''
#Conjunto
conjunto1 = {1,2,3,4,5,6,7,8,9,10}
print(conjunto1)

#Dicionario
dicionario1 = {}
dicionario1['nome:'] = 'zap'
dicionario1['idade'] = 78
print(dicionario1)

#Tuplas
tupla = ('uno', '0+0', 3, 'cuatro', 'five')
for i in tupla:
    print(i)
