class FilaCirculo:
    def __init__(self, tam):
        self.size = tam
        self.queue = [None] * tam
        self.front = self.rear = -1

    def ta_vazia(self):
        return self.front == -1

    def ta_cheio(self):
        return (self.rear + 1) % self.size == self.front

    def inserir(self, item):
        if self.ta_cheio():
            print("A fila está cheia.")
        elif self.ta_vazia():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def remover(self):
        if self.ta_vazia():
            print("A fila está vazia.")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return item

    def MenuFila(self):
        if self.ta_vazia():
            print("A fila está vazia.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()



if __name__ == "__main__":
    Fc = FilaCirculo(5)
    Fc.inserir(1)
    Fc.inserir(2)
    Fc.inserir(3)
    Fc.inserir(4)
    Fc.MenuFila()

    print("Primeira posição removida:", Fc.remover())
    Fc.MenuFila()

    Fc.inserir(5)
    Fc.inserir(6)
    Fc.MenuFila()
