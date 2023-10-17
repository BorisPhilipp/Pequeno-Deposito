class Veiculo:
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade

class Car(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

class Moto(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)
