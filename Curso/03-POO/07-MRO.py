# MRO = Method Resolution Order

class Abuelo:

    def saludar(self):
        print('Soy el abuelo')

class Padre(Abuelo):
    pass

class Madre:
    pass

class Hijo(Madre, Padre):

    def saludar(self):
        super(Hijo, self).saludar()

hijo = Hijo()

hijo.saludar()