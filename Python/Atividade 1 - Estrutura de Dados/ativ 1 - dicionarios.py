'''#1)Crie um dicionário vazio e adicione duas chaves e valores a ele.
meu_dicionario = {}
meu_dicionario['whatsapp'] = 'kung fu'
meu_dicionario['everson'] = 'zoio'

print(meu_dicionario)

========================================================================================= 

#2)Crie um dicionário com as chaves "nome", "idade" e "cidade" e preencha com
#seus dados. Imprima o dicionário.

dicionario = {'nome':[],'idade':[],'cidade':[]}
nome = input("Digite seu Nome: ")
idade = input("Digite sua Idade: ")
cidade = input("Digite sua Cidade: ")

dicionario.update({'nome': nome, 'idade': idade, 'cidade': cidade})
print(dicionario)

========================================================================================= 

#3)Crie um dicionário com o nome e o preço de três produtos diferentes.
#Imprima o dicionário.
produto = {
    "Produtos":['Mamão','Banana','Sabão'],
    "Preços":[5.94, 4.00, 6.75]}
produtosD = produto["Produtos"]
preços = produto["Preços"]
for i in range(len(produtosD)):
    produt = produtosD[i]
    prec = preços[i]
    print(f"Nome: {produt}     Preço: R$ {prec}")

=========================================================================================

#4)Crie um dicionário com o nome de três estados e suas respectivas capitais.
#Peça ao usuário para digitar um estado e imprima a capital correspondente.
estado = {'Paraná':'Curitiba', 'São Paulo':'São Paulo', 'Rio de Janeiro':'Rio de Janeiro'}
estadoDigitado = input("Digite Paraná, São Paulo ou Rio de Janeiro para aparecer suas respectivas capitais: ")
if estadoDigitado in estado:
    print(estado[estadoDigitado])
else:
    print("Não está no Dicionário.")

=========================================================================================

#5)Crie um dicionário com o nome de cinco cidades e suas respectivas
#populações. Imprima a cidade com a maior população.
dcCidades = {'Rio de Janeiro': 6500000, 'Guarapuava': 182644, 'Curitiba': 1773733, 'Pinhão': 32559 , 'São Paulo': 12000000}
print("A Cidade com maior população é: ",max(dcCidades))

=========================================================================================

#6)Crie um dicionário com o nome de três alimentos e suas respectivas calorias.
#Peça ao usuário para digitar um alimento e imprima a quantidade de calorias
#correspondente.
dcAlimentos = {'Ovo': 70, 'Banana': 100, 'Maça': 52}
print("Ovo, Banana, Maça")
print("Digite o Alimento para saber suas Calorias. ")
alimentoDigitado = input()
if alimentoDigitado in dcAlimentos:
    print(dcAlimentos[alimentoDigitado], "Kcal")
else:
    print("NÃO está no dicionário.")
{'Tucano': 'Ave', 'Girafa': 'Mamífero', 'Jacaré': 'Réptil', 'Sapo': 'Anfíbios', 'Bagre': 'Peixe'}

=========================================================================================

#7)Crie um dicionário com o nome de cinco animais e suas respectivas
#classificações (mamífero, ave, réptil, etc.). Imprima apenas os nomes dos
#animais.
animais = {"nomes":['Tucano','Girafa','Jacaré','Sapo','Bagre'],
            "class":['Ave','Mamífero','Réptil','Anfíbrios','Peixe']}
print(animais["nomes"])

=========================================================================================

#8)Crie um dicionário com o nome de cinco países e suas respectivas bandeiras.
#Imprima apenas os nomes dos países.
paises = {'Alemanha': 'https://s5.static.brasilescola.uol.com.br/be/2020/10/bandeira-da-alemanha.jpg',
          'Brasil': 'https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg',
          'Canadá': 'https://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Canada_%28Pantone%29.svg',
          'Índia': 'https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg',
          'Japão': 'https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg'}
for i in paises:
    print(i)

=========================================================================================

#9)Crie um dicionário com o nome de cinco frutas e suas respectivas cores.
#Imprima o nome de cada fruta seguido de sua cor.
frutas = {'Abacate': 'Verde',
          'Abacaxi': 'Amarelo',
          'Maça': 'Vermelho',
          'Laranja': 'Laranja',
          'Uva': 'Roxo'}
for nome,cor in frutas.items():
    print(f"{nome}, {cor}")

=========================================================================================

#10)Crie um dicionário com o nome de três jogos e a quantidade de jogadores
#necessária. Peça ao usuário para digitar um jogo e imprima a quantidade de
#jogadores correspondente.
jogos = {'Team Fortress 2': 105.398, 'Overwatch': 0, 'CSGO': 926.971}
print("Team Fortress 2, Overwatch💩, Counter Strike Global Offensive (CSGO).")
digitJogos = input("Digite o nome de um dos Jogos: ")
if digitJogos in jogos:
    print(jogos[digitJogos], "Jogadores")
    
=========================================================================================
'''