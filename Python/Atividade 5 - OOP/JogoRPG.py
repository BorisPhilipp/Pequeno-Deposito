import random
class Personagem:
    def __init__(self, nome, vida, dano):
        self._nome = nome
        self.__vida = vida
        self._dano = dano

    def atacar(self, inimigo):
        self._inimigo = inimigo
        print(f'{self._nome} ataca!')
        print(f'{inimigo._nome} sofre dano! {self._dano}')

        inimigo.reduzirVida(self._dano)

    def reduzirVida(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
    
    def reduzirDano(self):
        reducao = random.randint(1,9)
        self._dano -= reducao
        return self._dano
    
    def is_alive(self):
        return self.__vida > 0
    
    def Stats(self):
        print(f"Personagem: {self._nome}\nVida: {self.__vida}\nDano: {self._dano}")

    def curar(self):
        print(f'{self._nome} cura-se!')
        cure = random.randint(7,19)
        self.__vida += cure
        return self.__vida


class guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida= 80, dano= 14)

    def atacarEspecial(self, inimigo):
        damage = self._dano *2
        print(f'{self._nome} utiliza a Narsil!')
        print(f'e causa {damage} de dano!')
        inimigo.reduzirVida(damage)       

class magoBranco(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 110, dano = 19)

    def magiaEspecial(self, inimigo):
        print(f'{self._nome} usa a Lingua Negra de Mordor!')
        print(f'Dano do inimigo reduzido!')
        inimigo.reduzirDano()

class arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida= 70, dano= 10)

    def ataqueElfo(self, inimigo):
        damage = self._dano *2
        print(f'{self._nome} ataca rapidamente o Inimigo!')
        print(f'e causa {damage} de dano!')
        inimigo.reduzirVida(damage) 
        

