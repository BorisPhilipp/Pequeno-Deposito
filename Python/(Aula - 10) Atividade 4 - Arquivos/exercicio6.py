'''
6.Faça uma função que leia um arquivo texto
contendo uma lista de endereços IP e gere dois outros
arquivos, um contendo os endereços IP válidos e
outro contendo os endereços inválidos. O formato de
um endereço IP é num1.num.num.num, onde num1
vai de 1 a 255 e num vai de 0 a 255.
'''

def verifIP(IP_lista):
    listaIP = open(IP_lista, 'r')
    IPinvalido = open("6 - Lista de IPS Invalidos.txt", 'w')
    IPvalido = open("6 - Lista de IPS VALIDOS.txt", 'w')

    lista_IP_invalido = []
    lista_IP_valido = []

    ip = listaIP.readline()

    while ip != "":
        numeroIP = ip.split('.')

        if len(numeroIP) == 4:
            for i in range(4):
                oct = int(numeroIP[i])

                if i == 0 and not (1 <= oct <=255):
                    lista_IP_invalido.append(ip)
                    break
                else:
                    if i != 0 and not (0 <= oct <= 255):
                        lista_IP_invalido.append(ip)
                        break
                    elif i == 3 and (0<= oct <= 255):
                        lista_IP_valido.append(ip)
        else:
            lista_IP_invalido.append(ip)
        ip = listaIP.readline()

    IPinvalido.writelines(lista_IP_invalido)
    IPvalido.writelines(lista_IP_valido)

    IPinvalido.close()
    IPvalido.close()
    listaIP.close()

verifIP("6 - IPS.txt")
