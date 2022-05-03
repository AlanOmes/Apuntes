class Padre:

    def __init__(self, ojos, altura):
        self.ojos = ojos
        self.altura = altura

class Madre:

    def __init__(self, pelo, cejas):
        self.pelo = pelo
        self.cejas = cejas

class Hijo(Madre, Padre):

    def __init__(self, ojos, altura, pelo, cejas):
        Padre.__init__(self, ojos, altura)
        Madre.__init__(self, pelo, cejas)
