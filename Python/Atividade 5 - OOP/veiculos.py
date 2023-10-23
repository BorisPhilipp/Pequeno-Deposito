from Interface import Imprimivel
class Veiculo:
    def __init__(self, tipo, velocidade, descricao=None):
        self._tipo = tipo
        self._velocidade = velocidade
        self._descricao = descricao

    def descricao(self, texto_descricao = None):
        if self._descricao != None:
            print(self._descricao)
        else:
            if texto_descricao == None:
                print("Veiculo para transporte.")
            else:
                print(texto_descricao)
                self._descricao = texto_descricao


    def acelerar(self):
        print(f"Acelerando...")
        self._velocidade += 13
        print(f"Nova velocidade: {self._velocidade}")


class Car(Veiculo, Imprimivel):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

    def imprimir(self, fabricante, marca):
        print(f'{fabricante},{marca},{self._tipo},{self._velocidade},{self._descricao}')


class Moto(Veiculo, Imprimivel):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

    def imprimir(self, fabricante, marca):
        print(f'{fabricante},{marca},{self._tipo},{self._velocidade},{self._descricao}')