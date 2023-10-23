from abc import ABC, abstractmethod
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcular_area(self, largura, comprimento):
        return largura * comprimento
    
class circulo(Forma):
    def __init__(self):
        super().__init__()

    def calcular_area(self, R): #R = Raio
        return 3.14 * (R * R)