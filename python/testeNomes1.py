Nomes = {"Talion":"O Nunca-Morto",
         "Smeagol":"O Banido",
         "Gollum":"O Assassino",
         "Celebrimbor":"O Ferreiro-Elfo",
         "Sauron":"Senhor do Escuro",
         "Bilbo":"Bolseiro",
         "Frodo":"Bolseiro",
         "Gandalf":"O Mago Branco",
         "Gimli":"O Anao",
         "Aragorn":"O Rei de Gondor"}

valorNomes = Nomes.values()
def escreverNomes(Nomes, nomeArquivo):
    arquivoNomes = open(nomeArquivo, 'w')
    for i in Nomes:
        arquivoNomes.write(str(i))
        arquivoNomes.write(valorNomes(i))
        arquivoNomes.write("\n")
    arquivoNomes.close()
