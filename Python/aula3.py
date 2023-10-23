'''conta = int(input("Digite o número da conta:"))

while(conta != -1):
    saldo = float(input("Digite o saldo da conta:"))
    if saldo >= 10000:
        taxa = saldo * 0.001
    else:
        taxa = saldo * 0.003
    novoSaldo = saldo - taxa
    print("Valor dos serviços = {0:.2f}".format(taxa))
    print("Saldo Atual = {0:.2f}".format(novoSaldo))
    conta = int(input("Digite o número da conta:"))'''
'''
clienteNumero = 1
produtoValor = 0
descontos = 0

while clienteNumero <= 10:
    clienteNome = str(input(f"Cliente número {clienteNumero} Digite seu Nome: "))
    produtoValor = float(input("Insira o valor do produto: R$ "))

    if produtoValor >= 1500:
        descontoProduto = 0.2 * produtoValor
    elif produtoValor < 1500:
        descontoProduto = 0.15 * produtoValor

    descontos = descontos + descontoProduto
    print(f"Olá, {clienteNome}. O valor da compra é de R$ {produtoValor}. O desconto aplicado será de R$ {descontoProduto}, e o valor a ser pago R$ {produtoValor - descontoProduto}")
    clienteNumero = clienteNumero + 1

print(f"O total do desconto é R$ {descontos}")'''


