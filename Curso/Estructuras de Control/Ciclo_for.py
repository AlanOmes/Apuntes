# Teoría: ciclo for (ciclo incondicional)

# El for se usa cuando sabes la cantidad exacta de veces que queres ejecutar algo

'''for INDICE in range(CANTIDAD DE VECES QUE SE REPITE)
    Indice arranca de 0 y se increementa solo hasta que termina'''

lista = (1,2,3,4,5)
tupla = (1,2,3,4)
diccionario = {1:1, 2:2, 3:3}
texto = "hola"
numero = str(12345)

# Iterador - iteración
"""for letra in texto:
        print("Letra", letra)"""

# Con rangos - LO EJECUTA 5 VECES
"""for i in range(5):  
    print(i)
print ("-------")

for i in range(-5, 6, 2):
    print(i)"""

    # Enumeracion
for posicion, letra in enumerate(texto):
    print("La posicion es:", posicion)
    print("Y la letra es:", letra)


