#Estrutura Condicional Composta
temperatura = float(input("Informe a Temperatura:"))

if temperatura >= 30:
    print("Muito Calor")
elif temperatura >= 24:
    print("Calor")
elif temperatura >= 17:
    print("Temperatura Amena")
elif temperatura >=7:
    print("Temperatura Fria")
else:
    print("Muito Frio")

numero = int(input("Informe um valor: "))

if numero % 2 == 0 and numero > 0:
    print(f'{numero} é par')
elif numero % 2 != 0:
    print(f'{numero} é impar')
else:
    print(f'{numero} é zero')

