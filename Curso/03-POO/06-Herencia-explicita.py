class Padre:

    atributo_definido_en_la_clase = 'Soy el atributo definido de la clase'

    def __init__(self, argumento):
        self.atributo = argumento
    
    def un_metodo(self):
        return 'Soy el metodo de la clase padre'
    
class Hija:

    def __init__(self, argumento):
        Padre.__init__(self, argumento) # No hereda la clase, solo carga los atributos

hija = Hija('algo')

print(hija.atributo)