# Formateo

"""nombre = "Alan"
apellido = "Omes"
edad = "24 anios"
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

palabra = "hola" # Tamanio = 4 // Rango = T - 1 
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
print (palabra.lower()) # convierte la palabra a minuscula
print (palabra.title()) # si hay mas de una palabra en la variable, hace que todas empiecen en mayuscula

"""

# Eliminar la letra de una palabra por posicion 

'''

palabra = 'casa'
palabra = palabra[:2] + palabra[2 + 1:] # corta la palabra a partir de la posicion marcada y le suma el resto de la palabra
print (palabra) # Ejecuta : caa

'''

# Metodo split

"""palabra = "hola soy un texto"
print(palabra.split())"""

# Si quiero cortar o borrar determinada parte de una cadena de texto:

'''

a = "/casa/coche-je"
palabra = a.split("/")[-1].split("-")[0] 

print (palabra) #coche

'''

# Ingresar datos por teclado

print("¿Como se llama?")
nombre = input()
print(f"Juli le quiere dar a {nombre}")