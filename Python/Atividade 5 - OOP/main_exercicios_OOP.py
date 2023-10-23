#1
from Carro import Carro

car1 = Carro('Ford', 1987)
print("1----------")
print(car1.modelo)
print(car1.ano)
print(" ")

#2
car1.ano = 4564
car1.modelo = 'asdfghjkl'
print("2----------")
print(car1._Carro__modelo, car1._Carro__ano)
print(" ")

#3
from veiculos import Car, Moto
car2 = Car("4x4", 9)
moto2 = Moto('Moto', 6)
print("3----------")
print(car2._tipo)
print(f'{car2._velocidade} KM/H')
print(moto2._tipo)
print(f'{moto2._velocidade} KM/H')
print(" ")

#4
print("4----------")
car2.descricao()
moto2.descricao()
print("Com Descrição:")
car2.descricao("Um carro é um veículo terrestre de quatro rodas que oferece transporte pessoal ou de passageiros.")
moto2.descricao("Uma moto, ou motocicleta, é um veículo de duas rodas que oferece uma forma ágil e emocionante de locomoção.")
print("")

#5
print("5----------")
car2.acelerar()
moto2.acelerar()
print("")

#6
print("6----------")
lista_veiculos = [car2, moto2, moto2, car2]
for lista in lista_veiculos:
    lista.descricao()
print("")

print("7----------")
from Forma import retangulo, circulo
Retan = retangulo()
Circ = circulo()

#Retan.calcular_area(X), X = seu numero
#Circ.calcular_area(X, Y), X, Y = seu numero

print(f'{Retan.calcular_area(12, 7)} Area calculada do Retangulo.')
print(f'{Circ.calcular_area(15)} Area calculada do Circulo.')
print("")

print("8----------")
print("Carro:")
car2.imprimir("Uno", "Caindo aos pedaços")
print("")
print("Moto:")
moto2.imprimir("Motobike", "Arrasa quarteirão")
print("")

print("9----------")
from SistemaBanco import ContaBancaria
from ContasBanco import ContaPoupança, ContaCorrente

cliente1 = ContaCorrente("ShaolinMatadordePorco", 500)   #(Nome, Dinheiro)
cliente2 = ContaPoupança("FlavinDoPneu", 200, 0.10)       #(Nome, Dinheiro, Taxa)

print("Cliente 1---------------")
cliente1.transferir(100, "Carinha que mora logo ali")
cliente1.depositar(700)
cliente1.saque(800)
print("------------------------")
print("")
print("Cliente 2---------------")
cliente2.addjuros()
cliente2.transferir(100, "Kung Fu")
cliente2.depositar(900)
cliente2.saque(500)
print("------------------------")
print("")

print("10----------")
from JogoRPG import guerreiro, magoBranco, arqueiro
Gandalf = magoBranco("Gandalf")
Aragorn = guerreiro("Aragorn")
Legolas = arqueiro("Legolas")


Aragorn.Stats()
print()
Gandalf.Stats()
print()

Aragorn.atacar(Gandalf)
Aragorn.Stats()
print()
Gandalf.Stats()
print()

Gandalf.curar()
print()
Gandalf.Stats()
print()
Gandalf.magiaEspecial(Aragorn)
print()
Aragorn.Stats()
print()

Aragorn.atacarEspecial(Gandalf)
print()
Gandalf.Stats()
print()
Legolas.atacar(Aragorn)
print()
Aragorn.Stats()
print()
Legolas.ataqueElfo(Aragorn)
print()
Aragorn.Stats()