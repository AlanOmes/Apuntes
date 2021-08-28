# Formateo

"""nombre = "Alan"
apellido = "Omes"
edad = "24 años"
print ("hola mi nombre es:{0} {1} y mi edad es {2}".format(nombre,apellido,edad))
print (f"Hola, mi nombre es {nombre} {apellido} y mi edad es {edad}")"""


# Concatenar

"""nombre_completo = nombre + (" ") + apellido 
print ("Mi nombre es", nombre_completo)"""


# Slicing. 

'''
# Para saber la longitud de un string

palabra = 'Hola'
print(len(palabra)) # imprime la cantidad de letras que tiene el string 

'''

palabra = "hola" # Tamaño = 4 // Rango = T - 1 
print("Letra", palabra [0]) # h
print("Letra", palabra [1]) # o
print("Letra", palabra [2]) # l
print("Letra", palabra [3]) # a

print("Negativo:", palabra [-1]) # a
print("Negativo:", palabra [-2]) # l
print("Negativo:", palabra [-3]) # o
print("Negativo:", palabra [-4]) # h

print("Todos:", palabra[:])
print("Todos:", palabra [2:50]) # principio:final

print("Todos:", palabra[:])
print("Negativo:", palabra[::-1])

# Metodos

"""

palabra = "chau"
palabra = palabra.replace("c", "g") # reemplaza la c por la g
print(palabra) 
print(palabra.capitalize()) # empieza con mayuscula la palabra
print(palabra.find("h")) # devuelve la posicion de la letra en el string
print(palabra.upper()) # pasa la palabra a mayuscula 
print (palabra.lower()) # convierte la palabra a minúscula

"""

# Metodo split

"""palabra = "hola soy un texto"
print(palabra.split())"""

# Ingresar datos por teclado

print("¿Como se llama?")
nombre = input()
print(f"Juli le quiere dar a {nombre}")