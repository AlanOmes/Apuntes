# Teoria: tuplas

# Definir una tupla
tupla = (1, 2, 3, 4)

print(tupla)
print(f'Primer elemento: {tupla[0]}')

# Modificar el valor
print(f'Tupla sin modificar: {tupla}')
aux_lista = list(tupla)
aux_lista[0] = 999
tupla = tuple(aux_lista)
print(f'Tupla modificada: {tupla}')

