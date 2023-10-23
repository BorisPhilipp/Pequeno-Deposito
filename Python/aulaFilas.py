#Fila
#FIFO - First In First Out

#Inserção - no final
def enqueue(fila, elemento):
    fila.append(elemento)

#Remoção - no inicio
def dequeue(fila):
    if len(fila) == 0:
        return "A fila está vazia, não é possível remover."
    else:
        return fila.pop(0)

#Primeiro Elemento - Peek
def peek(fila):
    if len(fila) == 0:
        return "Fila vazia"
    else:
        return fila[0]

#Esta Vazio
def is_empty(fila):
    return len(fila)== 0

#Tamanho
def size(fila):
    return len(fila)

#Reverse
def queueReverse(fila):
    #return fila[::-1]
    filaReversa = []
    while not is_empty(fila):
        item = fila.pop() #dequeue(fila)
        enqueue(filaReversa, item)
    return filaReversa

fila = []
enqueue(fila,1)
enqueue(fila,2)
enqueue(fila,3)
#print(fila)
#print(dequeue(fila))
#print(peek(fila))
#print(is_empty(fila))
#print(size(fila))
#filaReversa = queueReverse(fila)
print(queueReverse(fila))




