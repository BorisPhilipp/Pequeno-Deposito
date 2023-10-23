from abc import ABC, abstractmethod

class transacao(ABC):
    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def transferir(self):
        pass

    @abstractmethod
    def saque(self):
        pass

class ContaBancaria(transacao):
    def __init__(self, usuario, grana = 0):
        self.__usuario = usuario
        self.__grana = float(grana)

    @property
    def grana(self):
        return self.__grana
    
    @grana.setter
    def grana(self, grana_novo):
        self.__grana = grana_novo

    def depositar(self, valor):
        if valor > 0:
            print(f'Foram depositados R${valor} na sua conta de {self.__usuario}, {self.grana + valor}.')
            self.grana += valor
        else:
            print("Insira uma quantia válida!")

    def saque(self, valor):
        if valor > 0:
            print(f'Foi retirado de sua conta R${valor}, restante: R${self.grana - valor}.')
            self.grana -= valor
        else:
            print("Insira uma quantia válida para o saque!")

    def transferir(self, valor, pessoa):
        if valor > 0:
            print(f'Foi transferido R${valor} para a conta bancária de {pessoa}, restando R${self.grana - valor}.')
            self.grana -= valor
        else:
            print("Insira uma quantia válida para a transferencia!")







# -=Caso ContasBanco.py não funcione=-
"""class ContaPoupança(ContaBancaria): 
    def __init__(self, usuario, grana=0, taxa= 0.03):
        super().__init__(usuario, grana)
        self.__taxa = taxa

    def addjuros(self):
        juros = self.grana * self.__taxa
        print(f'R${juros} juros aplicados sobre seu saldo de R${self.grana}, novo saldo de R${self.grana + juros}')
        self.grana += juros
    
class ContaCorrente(ContaBancaria):
    def __init__(self, usuario, grana=0):
        super().__init__(usuario, grana)"""
