# Ejercicio 1: Crear una clase llamada Persona donde sus atributos van a ser: 

# Atributos: 
#      - Nombre
#      - Edad
#      - DNI

# Y va a tener los siguientes métodos:
# - mostrarEdad(): devuelve la edad de la persona
# - esMayorDeEdad: devuelve True si es mayor o igual a 18, y False si es menor de 18

# Realizar su respectivo metodo, constructor y atributos.

'''

class Persona:
    
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrarEdad(self):
        return self.edad
    
    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        return False

alan = Persona('Alan', 26, '39641877')

print(alan.mostrarEdad())
print(alan.esMayorDeEdad())

'''

# Ejercicio 2: Crear una clase llamada Calculadora donde no va a tener ningun atributo pero va a contener los siguientes metodos: 

# Metodos:
#   - sumar(n1, n2)
#   - restar(n1, n2)
#   - dividir(n1, n2)
#   - multiplicar(n1, n2)

'''

class Calculadora:
    
    def sumar(self, n1, n2):
        return n1 + n2
    
    def restar(self, n1, n2):
        return n1 - n2
    
    def dividir(self, n1, n2):
        return n1 / n2

    def multiplicar(self, n1, n2):
        return n1 * n2

calculadora = Calculadora()

print(calculadora.sumar(5, 5))
print(calculadora.restar(10, 5))
print(calculadora.dividir(10, 5))
print(calculadora.multiplicar(5, 5))

'''

# Ejercicio 3: Crear una clase llamada ListaDeTareas donde no va a recibir ningun argumento en su constructor, pero va a tener un argumento definido como una lista, y va a contener los siguientes metodos:

# Metodos: 
#   - mostrarTarea()
#   - agregarTarea(tarea)
#   - quitarTarea(tarea)

'''

class ListaDeTareas:

    lista_de_tareas = []

    def mostrarTareas(self):
        return self.lista_de_tareas
    
    def agregarTarea(self, tarea):
        self.lista_de_tareas.append(tarea)
        print('Tarea agregada con éxito.')
    
    def quitarTarea(self, tarea):
        if tarea in self.lista_de_tareas:
            self.lista_de_tareas.remove(tarea)
            print('Tarea eliminada con éxito.')
        else:
            print('La tarea que quisiste quitar, no existe.')

cuaderno = ListaDeTareas()

print(cuaderno.mostrarTareas())

cuaderno.agregarTarea('Salir a jugar')
cuaderno.agregarTarea('Practicar Python')
cuaderno.agregarTarea('Jugar al pes')

print(cuaderno.mostrarTareas())

cuaderno.quitarTarea('Salir a jugar')
cuaderno.quitarTarea('Tarea que no existe')

print(cuaderno.mostrarTareas())

'''

# Ejercicio 4: Crear una clase llamada Revertir donde va a recibir una lista de palabras, y luego, podrá transofmar esa lista en un string con las palabras invertidas, ejemplo:

# ['Hola', 'como', estas'] -> 'estas como Hola'

# Atributos:
#    - listaDePalabras

# Metodos:
#    - revertir()
#    - mostrarFrase()

'''

class Revertir:
    
    def __init__(self, listaDePalabras):
        self.listaDePalabras = listaDePalabras
    
    def revertir(self):
        aux = self.listaDePalabras[::-1] # ['estas', 'como', 'Hola']
        self.listaDePalabras = ' '.join(aux) # 'estas como Hola'
        print('Valor revertido.')

    def mostrarFrase(self):
        return self.listaDePalabras

lista = ['Hola', 'como', 'estas']
revertir = Revertir(lista)
print(revertir.mostrarFrase())
revertir.revertir()
print(revertir.mostrarFrase())

'''

# Ejercicio 5: simular una pelea entre los guerreros Z, en el cual va a tener las siguientes clases:

# - Luchador: clase concreta de la cual van a instanciar todos los guerreros y va a contener: 
#   * Atributos:
#       - Nombre (del luchador): str
#       - Ki: int
#       - SSJ: booleano
#       - Ataque: int
#       - Defensa: int
#       - Vida: int

#   * Metodos:
#       - Atacar

# Batalla: clase que vamos a utilizar como menu, donde va a recibir dos luchadores y va a empezar la batalla por turnos

# - Ejemplos:

#   Goku:
#       - Nombre: Goku
#       - Ki: 9000
#       - SSJ: True
#       - Ataque: 1000
#       - Defensa: 500
#       - Vida: 1000

#   MajinBoo:
#       - Nombre: Majin Boo
#       - Ki: 7500
#       - SSJ: False
#       - Ataque: 700
#       - Defensa: 700
#       - Vida: 1500

import time

class Luchador:
    def __init__(self, nombre, ki, ssj, ataque, defensa, vida):
        self.nombre = nombre
        self.ki = ki
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        print(f'El luchador {nombre} está listo para pelear!')
    
    def atacar(self, enemigo):
        print(f'La vida de {enemigo.nombre} es: {enemigo.vida}')
        diferencia_de_ataque = self.ataque - enemigo.defensa
        enemigo.vida -= diferencia_de_ataque
        print(f'{self.nombre} atacó a {enemigo.nombre} con {diferencia_de_ataque} de ataque.')
        print(f'La vida de {enemigo.nombre} es: {enemigo.vida}')

class Batalla:

    turno = '1'

    def __init__(self, luchador1, luchador2):
        self.luchador1 = luchador1
        self.luchador2 = luchador2

    def comenzarBatalla(self):
        while self.luchador1.vida > 0 and self.luchador2.vida > 0:
            time.sleep(1)
            if self.turno == '1':
                self.luchador1.atacar(self.luchador2)
                self.turno = '2'
            else:
                self.luchador2.atacar(self.luchador1)
                self.turno = '1'
        if self.luchador1.vida <= 0:
            print(f'El ganador es: {self.luchador2.nombre}')
        else:
            print(f'El ganador es: {self.luchador1.nombre}')


goku = Luchador('Goku', 9000, True, 1000, 500, 1000)
majinboo = Luchador('Majin Boo', 7500, False, 700, 700, 1500) 

Batalla(goku, majinboo).comenzarBatalla()
