'''
5.Faça um programa para alterar uma das notas de
um aluno (usando os arquivos do exercício anterior).
O programa deve ter uma função que recebe o nome
do aluno, a nota velha e a nova nota. A função deve
fazer a alteração no arquivo.
'''

def idcNomes(aluno, lista_nomes):
    for i in lista_nomes:
        if aluno == i:
            indice = lista_nomes.index(i)
            return indice

def idcNotas(indice, lista_notas):
    for i in range(len(lista_notas)):
        if i == indice:
            return lista_notas[i]

def alterarNotas(arquivoNotas, arquivoNomes, nomeAluno, novaNota):
    nomes5 = open(arquivoNomes, 'r')
    notas5 = open(arquivoNotas, 'r+')
    nota_Nova = novaNota
    aluno = nomeAluno+'\n'

    nomes = nomes5.readlines()
    notas = notas5.readlines()
    
    if aluno in nomes:
        print("Nome encontrado!\nDeseja alterar a nota? [S]/[N]: ", end='')
        confirmacao = input()
        if confirmacao == 's' or 'S':
            indice_aluno = idcNomes(aluno, nomes)
            notas_na_lista = idcNotas(indice_aluno, notas)
            
            print(f"Notas encontradas: {notas_na_lista}")
            
            notas5.close()
            
            print(f"Atualizando notas...")
            
            notas5 = open(arquivoNotas, 'w')
            notas.remove(notas_na_lista) # type: ignore
            notas[indice_aluno] = nota_Nova # type: ignore
            notas5.writelines(notas)
            
            print(f"Notas atualizadas: {idcNotas(indice_aluno, notas)}")
    else:
        print(f"Nome não encontrado! {nomes}")
    nomes5.flush()
    notas5.flush()

alterarNotas("4 - notas.txt","4 - nomes.txt", "Gollum", "2.0 2.1 2.2\n")
