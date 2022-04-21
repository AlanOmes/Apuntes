class Padre:

    def metodo_1(self):
        print('Soy el print de la clase padre')

class Hija(Padre):
    
    def metodo_1(self):
        print('Soy el print de la clase hija')

hija = Hija()
hija.metodo_1()