from SistemaBanco import ContaBancaria

class ContaPoupança(ContaBancaria):
    def __init__(self, usuario, grana=0, taxa= 0.03):
        super().__init__(usuario, grana)
        self.__taxa = taxa

    def addjuros(self):
        juros = self.grana * self.__taxa
        print(f'R${juros} juros aplicados sobre seu saldo de R${self.grana}, novo saldo de R${self.grana + juros}')
        self.grana += juros
    
class ContaCorrente(ContaBancaria):
    def __init__(self, usuario, grana=0):
        super().__init__(usuario, grana)