# Teoria

# Definir funcion 
def nombre(parametro:str) -> str:
    print(parametro)
    return parametro

# Procedimiento
def procedimiento(parametro):
    print(parametro)

# Funcion
def funcion(parametro):
    return parametro

# Funcion que sume dos numeros
def mostrar_suma(n1, n2):
    print (f'La suma es {n1 + n2}')

mostrar_suma(2, 2)

def obtener_suma(n1, n2):
    return n1 + n2

resultado = obtener_suma(50, 50)
print(f'El resultado es: {resultado}')

# Propiedades

def argumentos(*args):
    print(args)

argumentos(1,2,3,4)

def kargumentos(**kwargs):
    print(kwargs)

kargumentos(a=3, b=4, c='hola', d='prueba', cualquiera='cualquiera')