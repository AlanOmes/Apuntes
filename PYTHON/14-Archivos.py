def app():
    # Crear el archivo
    archivo = open('Archivo.txt', 'w') # w es escritura, si no existe lo creara

    # Generar numeros en archivo
    for i in range (0, 20):
        archivo.write(f'Esta es la linea {str(i)}\r')
    
    # Cerrar el archivo
    archivo.close()

app() 