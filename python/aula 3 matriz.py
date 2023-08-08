nomes = ["Valdir","Nilson","Armindo","Jarme","Antonio"]
idades = [42,47,49,50,51]

#Média
soma = 0

for idade in idades:
    soma += idade
media = soma/len(idades)

for i in range (len(idades)):
    if idades[i] > 18:
        print("Veio que é velho pra caraio: ", nomes[i],"-",idades[i])


