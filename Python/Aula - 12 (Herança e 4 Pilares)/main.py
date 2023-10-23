from Cachorro import Cachorro
from Gato import Gato
from Professor import Professor
from Aluno import Aluno

c1 = Cachorro("Byte", "Chihuahua")
g1 = Gato("Get","Cinza")

p1 = Professor("Alan Turing")
a1 = Aluno("Gerso")

c1.emitirSom()
g1.emitirSom()

c1.buscar()
g1.arranhar()

print(p1.saudar())
print(a1.saudar())
