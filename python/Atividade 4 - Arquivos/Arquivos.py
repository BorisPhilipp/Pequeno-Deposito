import random
# Exercicio - 1
"""
1.Faça um programa que leia um número N e gere um arquivo com N nomes e idades aleatórios
⦁ Faça uso de duas listas criadas na mão: uma que contenha 20 nomes e outra que contenha 20 sobrenomes
⦁ Cada linha do arquivo resultante deve conter um nome completo e a sua idade"""

Nomes = ["Talion","Smeagol","Gollum","Celebrimbor","Sauron","Bilbo","Frodo","Gandalf","Gimli","Aragorn","Legolas","Thorin","Saruman","Galadriel","Elrond","Pippin","Samwise Gamgee","Boromir","Faramir","Radagast","Merry"]
Sobrenomes = ["O Nunca-Morto","O Banido","O Assassino","O Ferreiro-Elfo","Senhor do Escuro","Bolseiro","Bolseiro","O Mago Branco","O Anao","O Rei de Gondor","O Elfo Arqueiro","Ultimo Herdeiro de Durin","Ultimo Mago Branco","A Mais Pura e Justa","Rei dos Elfos da Floresta","O Peregrino Tolo","Melhor Amigo de Frodo","O Humano","Irmao de Boromir","O Castanho","Amigo de Pippin"]
digit = int(input("Digite a quantidade de Soldados que você precisa. (0 - 20): "))

def escreverNomes(nomeArquivo):
    arquivoNomes = open(nomeArquivo, 'w')
    arquivoNomes.write(f'{"NOMES":<17} {"SOBRENOMES":<23} {"IDADES":>8}\n')

    for i in range(digit):
        aleatorio = random.randint(0,20)
        aleatorioSobre = random.randint(0,20)
        SobrenomesA = str(Sobrenomes[aleatorioSobre])
        nomesA = str(Nomes[aleatorio])
        idades = random.randint(0,100)
        terraMedia = f"{nomesA:<17} {SobrenomesA:<23} {idades:>8}\n"
        arquivoNomes.write(terraMedia)
    arquivoNomes.close()


# Exercicio - 2
"""2.Estenda o exemplo do cadastro para considerar também a altura da pessoa"""

def Alturas(nomeArquivo):
    arquivoNomes = open(nomeArquivo, 'a')    
    arquivoNomes.write("\n")
    arquivoNomes.write("ALTURAS")
    arquivoNomes.write("\n")

    for i in range(digit):                  #For que faz aparecer alturas aleatorias
        arquivoNomes.write(str(round(random.uniform(1.00, 2.10),2)))
        arquivoNomes.write(str("\n"))
    arquivoNomes.close()
escreverNomes('nomes.txt')

choice = input("Deseja adicionar as alturas?(S/N): ").lower()
if choice == 's':
    Alturas('nomes.txt')
else:
    exit()
