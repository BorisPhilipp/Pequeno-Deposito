class Veiculo:
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade

class Descricao:
    print("É um Automóvel automatizado de extrema automatização")

class Car(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

class Moto(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)
