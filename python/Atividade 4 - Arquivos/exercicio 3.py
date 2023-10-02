#3. Escreva uma função que recebe dois nomes de arquivos e
#copia o conteúdo do primeiro arquivo para o segundo arquivo.
#Considere que o conteúdo do arquivo de origem é um texto.
#Sua função não deve copiar linhas comentadas (que
#começam com //)

def copiar(arquivoOriginal, arquivoCopiado):
    original = open(arquivoOriginal, 'r')
    copiado = open(arquivoCopiado,'w')
    ler = original.readline()

    while ler != "":
        if ler.startswith("#"):
           ler = original.readline()
        else:
            copiado.write(ler)
            copiado.write("\n")
            ler = original.readline()
        
    original.close()
    copiado.close()

copiar("arquivoOriginal.txt", "arquivoCopiado.txt")




