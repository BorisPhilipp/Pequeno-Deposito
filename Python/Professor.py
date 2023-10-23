from Pessoa_abc import Pessoa

class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self._nome = nome
    def saudar(self):
        return f'Olá, eu sou o prof {self._nome}'

