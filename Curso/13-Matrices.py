# Teoria: listas y matrices

matriz = [[1,2,3], [4, 5, 6], [7, 8, 9]]

# Mostrar matriz
for fila in matriz:
    print(*fila)

# Cantidad de filas
tamanio_filas = len(matriz)

# Cantidad de columnas
tamanio_columnas = len(matriz[0])
print(f'Cantidad de filas: {tamanio_filas}')
print(f'Cantidad de columnas: {tamanio_columnas}')

# Mostrar fila
print(f'Fila 1: {matriz[0]}')
print(f'Fila 1 - Columna 3: {matriz[0][2]}') # Primer num: num de la fila, segundo num: num de la columna
