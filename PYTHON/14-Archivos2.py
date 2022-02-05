def app():
    with open('Archivo.txt') as archivo: 
        for contenido in archivo:
            print (contenido.rstrip())

app()