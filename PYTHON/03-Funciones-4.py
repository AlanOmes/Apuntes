nombre = "Alan"

def mostrar_nombre(nombre):
    print (f'Hola {nombre}')

mostrar_nombre(nombre)

print (nombre.upper())

print ("----------------------")

# RETO
# Crea una funcion que imprima un mensaje de bienvenida
# Crea una función que tome un nombre de un usuario y lo muestre como mensaje de bienvenida
# Crea una función que tome la última actividad que hiciste 

def mensajeBienvenida():
    print ('Bienvenido!')

nombre = input('Ingrese su nombre:')

def informacion(mensaje_bienvenida, nombre):
    print (f"Queremos darte la {mensaje_bienvenida}, {nombre}")

informacion ('bienvenida', nombre)