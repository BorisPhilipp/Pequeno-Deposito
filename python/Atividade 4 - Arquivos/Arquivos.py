import random
"""
def escreverNumerosAleatorios(qtdNumeros, nomeArquivo):
    arquivoNumeros = open(nomeArquivo, 'w')
    for i in range(qtdNumeros):
        arquivoNumeros.write(str(random.randint(0,100)))
        arquivoNumeros.write("\n")

    arquivoNumeros.close()

escreverNumerosAleatorios(100, 'aleatorios.txt')

def escreverMedia(qtdNumeros, nomeArquivo):
    arquivoNumeros = open(nomeArquivo)
    soma = 0

    for i in range(qtdNumeros):
        num = float(arquivoNumeros.readline())
        soma += num
    arquivoNumeros.close()
    return soma/qtdNumeros
print(escreverMedia(3, 'media.txt'))
"""
"""
def copiaArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, 'r')
    f2 = open(novoArquivo, 'w')
    for texto in f1:
        f2.write(texto)
    f1.close()
    f2.close()

copiaArquivo('media.txt', 'novoMedia.txt')
"""
# Exercicio - 1
Nomes = ["Talion","Smeagol","Gollum","Celebrimbor","Sauron","Bilbo","Frodo","Gandalf","Gimli","Aragorn"]
Sobrenomes = ["O Nunca-Morto","O Banido","O Assassino","O Ferreiro-Elfo","Senhor do Escuro","Bolseiro","Bolseiro","O Mago Branco","O Anao","O Rei de Gondor"]

def escreverNomes(Nomes, nomeArquivo):
    arquivoNomes = open(nomeArquivo, 'w')
    arquivoSobrenomes = open(nomeArquivo, 'a')
    for i in Nomes:
        arquivoNomes.write(str(i))
        arquivoNomes.write("\n")

    for i in Sobrenomes:
        arquivoSobrenomes.write(str(i))
        arquivoSobrenomes.write("\n")
    arquivoNomes.close()

escreverNomes(Nomes, 'nomes.txt')

