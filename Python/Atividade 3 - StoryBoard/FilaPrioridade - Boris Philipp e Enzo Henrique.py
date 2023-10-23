class FilaPrioriedade:
    def __init__(self):
        self.elemnt = []

    def ta_vazio(self):
        return len(self.elemnt) == 0

    def insere(self, item, prioridade):
        self.elemnt.append((item, prioridade))

    def remove(self):
        if self.ta_vazio():
            print("A fila de prioridade está vazia.")
        return self.elemnt.pop(0)[0] 



Fp = FilaPrioriedade()
Fp.insere('Exemplo 1', 3)
Fp.insere('Exemplo 2', 1)
Fp.insere('Exemplo 3', 2)

while not Fp.ta_vazio():
    item = Fp.remove()
    print(f'Tarefa: {item}')
