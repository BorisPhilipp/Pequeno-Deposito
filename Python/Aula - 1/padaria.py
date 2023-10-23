print("Quantidade de Pães vendidos")
pao = input()
print("Quantidade de Broas vendidas")
broa = input()

preçototaldePao = float(pao) * 0.80
preçototaldeBroa = float(broa) * 2.50

totalAmbos = float(preçototaldeBroa + preçototaldePao)
fabricacao = float(0.43 * totalAmbos)
totalPoupanca = float((totalAmbos - fabricacao) * 0.15)
ViagemReal = float((totalAmbos - fabricacao - totalPoupanca) * 0.15)
ViagemEuro = float(ViagemReal / 4.60)
lucro = float((totalAmbos - fabricacao - totalPoupanca - ViagemReal))

print("Total de Pães vendidos: ",pao)
print("Total de Broa vendidos: ",broa)
print("O total vendido é: ",totalAmbos)
print("O valor da poupança é: R$ {totalPoupanca:.2f}".format(totalPoupanca = totalPoupanca))
print("O valor da viagem em reais é: R$ {ViagemReal:.2f}".format(ViagemReal = ViagemReal))
print("O valor da Viagem convertido para Euro é: £ {ViagemEuro:.2f}".format(ViagemEuro = ViagemEuro))
print("Lucro: R$ {lucro:.2f}".format(lucro = lucro))
