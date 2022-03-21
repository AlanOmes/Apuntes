# Teoria: listas y matrices

'''

# Crear una lista 

lista = [1, 2, 3, 4, 'hola', 2.4, True, False]
tamanio = len(lista)
print (f'Tamaño de la lista: {tamanio}')

# Posiciones
print(f'Primer elemento de la lista: {lista[0]}')

ultima_posicion = tamanio - 1
print(f'El ultimo elemento de la lista es: {lista[ultima_posicion]}')

# Slicing
print (f'Slicing, ultimo elemento: {lista[-1]}')
print(f'Slicing, primer elemento: {lista[-8]}')
print(f'Slicing, ver todos los elementos: {lista[:]}') # lista[principio:final]
print(f'Slicing, ver todos los elementos: {lista[0:]}')
print(f'Slicing, ver todos los elementos: {lista[0:8]}')

# Dar vuelta una lista

print(f'Slicing, dada vuelta: {lista[::-1]}')

# Propiedades
# Iteracion

texto = ['Hola', 'mi nombre', 'es', 'Alan']

for palabra in texto:
    print(f'{palabra} ', end="")

print('---------------')

for palabra in range(len(texto)):
    print(f'Posicion {palabra} - Palabra {texto[palabra]}')

# Ordenar una lista

lista_desordenada = [2, 6, 21, 8, 25, 3, 8, -123]
print (f'Lista desordenada: {lista_desordenada}')
lista_desordenada.sort()
print(f'Lista ordenada: {lista_desordenada}')

# Otra manera

lista_ordenada = sorted(lista_desordenada, reverse = True) # De mayor a menor
print(f'Lista ordenada: {lista_ordenada}')

'''

# Añadir elementos 

# Usando append

lista_vacia = []
print(f'Lista vacia: {lista_vacia}')
lista_vacia.append(1)
lista_vacia.append(2)
lista_vacia.append(3)
print(f'Lista con datos: {lista_vacia}')

# Usando insert
lista_vacia.insert(1, 4) # primer num: posicion en la que quiero agregar, segundo: num que quiero agregar
print(f'Lista con insert: {lista_vacia}')

# Usando extend
lista_vacia.extend([5, 6, 7])
print(f'Lista con extend: {lista_vacia}')

# Eliminar datos con pop
capturar = lista_vacia.pop(0)
print(f'La nueva lista con pop: {lista_vacia}')
print (f'Y lo capture aqui: {capturar}')

# Eliminar datos con del
del lista_vacia[0]
print(f'Eliminado con del: {lista_vacia}')

# Modificar
lista_vacia[-1] = 999
print(f'Lista modificada: {lista_vacia}')

# Buscar
posicion = lista_vacia.index(999)
print(f'La posicion de 999 es: {posicion}')