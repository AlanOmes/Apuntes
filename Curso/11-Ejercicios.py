# Ejercicio 4

# Escribir un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima por la 
# pantalla en lineas distintas el nombre del usuario tantas veces como el numero intruducido.

'''

nombre = input("Ingresa tu nombre: ")
numero = int(input("Ingresa un numero: ")) 
for i in range(numero):
    print(nombre)
    
'''


# Ejercicio 5

# Escribir un programa que pregunte el nombre del usuario en la consola y despues de que el usuario lo 
# intdoruzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
# mayusculas y <n> es el numero de letras que tienen el nombre 


'''

nombre = input ("Ingresa tu nombre: ") # guarda el nombre que ingrese el usuario
nombre = nombre.upper()
cantidad_letras = len(nombre) # se guarda la cantidad de letras que tiene nombre, en la var cant_letras
print (nombre, "tiene", cantidad_letras, "letras") 

'''

# Ejercicio 6 

# Escribir un programa que pregunte al usuario por el numero de horas trabajadas y el coste por hora
# Despues mostrar por pantalla la paga que le corresponde 

""" 

precio_por_hora = int (input("Ingresa el costo por hora: "))
horas_trabajadas = int (input("Ingresa la cantidad de horas trabajadas: "))
print ("El total a cobrar es: ", precio_por_hora * horas_trabajadas)

"""

# Ejercicio 7

# Pedir el precio de un producto y calcular su IVA (21%) y su valor original

"""
precio = int (input ("Ingresa el precio del producto: "))
iva = 21 * (precio) / 100
total = iva + precio

print ("Valor original:",precio)
print ("IVA:", iva )
print ("Precio total:", total)

"""

# Ejercicio 8 

# Ingresar dos numeros y mostrar el menor de ellos

"""

numero1 = int (input ("Ingrese un numero:"))
numero2 = int (input ("Ingrese un numero:"))



if numero1 > numero2:
    print("El numero menor es:", numero2)
elif numero1 == numero2:
    print ("Los numeros son iguales")
else:
     print("El numero menor es:", numero1) 
     
    
"""

# Ejercicio 9 

# Pedir al usuario su edad y mostrar si es mayor de edad o no

"""

edad = int (input ("Ingrese su edad:"))
numero = 18

if edad >= numero:
    print ("Es mayor de edad")
else:
    print ("Es menor de edad")

"""

# Ejercicio 10

# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

"""

palabra = (input("Ingrese una palabra:"))

for i in range (10):
    print (palabra)

"""


# Ejercicio 11

# Escribir un programa que pida al usuario un numero entero y muestre por pantalla si es par o impar

"""

numero = int(input ("Ingrese un numero:"))

par = numero % 2 

if par == 0:
    print ("El numero es par")
else:
    print ("El numero es impar")

"""


# Ejercicio 12

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números
# impares desde 1 hasta ese número separado por comas

"""

numero = int (input ("Ingrese un numero:"))

for i in range (1, numero+1, 2):
    print (i, end=", ")
    

"""

# Ejercicio 13

# Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras
# desde ese numero hasta cero separado por comas

"""

numero = int (input("Ingrese un numero:"))

for i in range (-numero, 0+1): 
    print (i * -1, end=", ")
print ("---")
for i in range (numero, -1, -1):
    print (i, end=  ", ")

"""

# Ejercicio 14

#  Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo

"""

signo = (input ("Ingrese un signo:"))
numero = int (input ("Ingrese un numero:"))

for j in range (numero + 1):
        for i in range (j):
         print (signo, end= (""))
        print ("")
   

"""




# Ejercicio 15

# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

"""

for i in range (1, 10 + 1):
    print (i, "* 1 =", i * 1)
    print (i, "* 2 =", i * 2)
    print (i, "* 3 =", i * 3)
    print (i, "* 4 =", i * 4)
    print (i, "* 5 =", i * 5)
    print (i, "* 6 =", i * 6)
    print (i, "* 7 =", i * 7)    
    print (i, "* 8 =", i * 8)
    print (i, "* 9 =", i * 9)
    print (i, "* 10 =", i * 10)
    print ("-------")

"""


# Ejercicio 16

# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la
# palabra introducida empezando por la última 


"""

palabra = input ("Ingrese una palabra:")

posicion = len(palabra)-1
while (posicion >= 0):
    print (palabra [posicion])
    posicion -= 1

print ("-----------")

posicion = len (palabra) -1
for posicion in range (posicion, -1, -1):
    print (palabra [posicion])


"""


# Ejercicio 17

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla
# el numero de veces que aparece la letra en la frase

'''

frase = input ("Escriba una frase:")
letra = input ("Elija una letra:")
longitud = len(frase)

for i in frase:
     if i == letra:
        print ()

'''