# Teoria: Diccionarios

# Definir un diccionario

diccionario = {
    'rojo' : 'red',
    'azul' : 'blue',
    'amarillo' : 'yellow'
}

# Mostramos
print(f'El color rojo en inglés es: {diccionario["rojo"]} ')
print(f'El color azul en inglés es: {diccionario["azul"]}')
print(f'El color amarillo en inglés es: {diccionario["amarillo"]}')

# Agregar
diccionario["verde"] = "grin"
diccionario.update({"blanco" : "white"})
print (diccionario)

# Modificar
diccionario["verde"] = "green"
diccionario.update({"verde" : "green"})

# Obtener con el metodo
rojo = diccionario.get("rojo")
print(f'El color rojo es: {rojo}')

# Eliminar
del diccionario["azul"]
diccionario.pop("verde")
print(diccionario)

# Items
print(f'Items: {diccionario.items()}')
# Keys
print(f'Keys: {diccionario.keys()}')
# Values
print(f'Values: {diccionario.values()}')

for items in diccionario.items(): # Devuelve tuplas
    print(items) 

for key, value in diccionario.items(): # Devuelve llave y valor
    print(key, value)

for key in diccionario.keys(): # Devuelve las llaves
    print(key)

for value in diccionario.values(): # Devuelve los valores
    print(value)