class Animal:
    
    def __init__(self, especie):
        self.especie = especie
    
    def comer(self):
        print('Estoy comiendo')
    
    def respirar(self):
        pass 

class Pajaro(Animal):

    def volar(self):
        pass

class Conejo(Animal):

    def correr(self):
        pass

pajaro = Pajaro("Ave")
pajaro.comer()