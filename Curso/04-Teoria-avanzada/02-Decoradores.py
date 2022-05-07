# Decoradores

'''

def decorar_arbol(arbolito):
    
    def luces():
        print('*Agregando luces*')

    def estrellita():
        print('*Agregando estrellita*')

    luces()
    estrellita()
    return arbolito

@decorar_arbol # Captura la funcion de abajo
def arbolito():
    print('Soy un arbolito :)')

arbolito()

'''


class A:
    
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, argumento):
        print('*Modificando el atributo*')
        self.__nombre = argumento

    @nombre.getter
    def nombre(self):
        print('*Devolviendo el atributo*')
        return self.__nombre

    @nombre.deleter
    def nombre(self):
        print('*Eliminando el atributo*')
        del self.__nombre

a = A('Alan')
print(a.nombre) # getter

a.nombre = 'Julieta' # setter
print(a.nombre)

del a.nombre # deleter


