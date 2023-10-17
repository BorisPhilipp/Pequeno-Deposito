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
car2 = Car('4x4', 9)
moto2 = Moto('Moto', 6)
print("3----------")
print(car2._tipo)
print(f'{car2._velocidade}km')
print(moto2._tipo)
print(f'{moto2._velocidade}km')
print(" ")

#4




