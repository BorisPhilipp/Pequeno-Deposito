'''
4. Faça um programa contendo uma função que recebe como
argumentos os nomes de dois arquivos. O primeiro arquivo
contém nomes de alunos e o segundo arquivo contém as
notas dos alunos. No primeiro arquivo, cada linha
corresponde ao nome de um aluno e no segundo arquivo,
cada linha corresponde às notas dos alunos (uma ou mais).
Assuma que as notas foram armazenadas como strings, e
estão separadas umas das outras por espaços em branco.
Leia os dois arquivos e gere um terceiro arquivo que contém o
nome do aluno seguido da média de suas notas.
'''

def Media(nomes4, notas4):
    nomes = open(nomes4, 'r')
    notas = open(notas4, 'r')
    nomesNotas = open("4 - Media.txt", 'w')

    lerNomes = nomes.readline()
    lerNotas = notas.readline()

    while lerNotas != "":
        listaNotas = lerNotas.split(" ")
        nome = lerNomes.replace("\n", "")
        soma = 0.0

        for i in listaNotas:
            idc = listaNotas.index(i)
            if "\n" in i:
                listaNotas[idc] = listaNotas[idc].replace("\n", "")
            soma += float(listaNotas[idc])

        media = "{:.2f}".format(soma/3)
        mediaAluno = f'{nome:<20} {media}\n'
        nomesNotas.write(mediaAluno)
        lerNotas = notas.readline()
        lerNomes = nomes.readline()

    nomesNotas.close()
    nomes.close()
    notas.close()

Media('4 - nomes.txt', '4 - notas.txt')