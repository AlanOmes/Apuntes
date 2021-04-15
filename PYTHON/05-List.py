lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

''' print (lenguajes) '''

# Los arrays (lists) comienzan en la posición 0
''' print (lenguajes [0]) ''' # Python

# Ordenar los elementos
''' 

lenguajes.sort() # Ordena alfabéticamente

print (lenguajes)

'''

# Acceder a un elemento dentro de un texto

'''

aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print (aprendiendo)

''' 

# Modificando valores de una lista 

'''

lenguajes[2] = 'PHP'
print (lenguajes)

'''

# Agregar elementos a una lista

'''

lenguajes.append('Ruby')
print (lenguajes)

'''

# Eliminar de una lista

'''

del lenguajes[1]
print(lenguajes)

'''

# Eliminar de una lista

'''

lenguajes.pop() # Eliminar el último elemento
print (lenguajes)

'''

# Eliminar con pop una posición en específico

'''

lenguajes.pop(0)
print (lenguajes)

'''

# Eliminar por nombre

'''

lenguajes.remove ('Python')
print (lenguajes)

'''