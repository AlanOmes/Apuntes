from distutils import extension
from logging import exception
import os

CARPETA = 'Contactos/' # Carpeta de Contactos
EXTENSION = '.txt' # Extension de archivos

# Contactos

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menu de opciones
    mostrar_menu()

    # Preguntar al usuario la accion a realizar

    preguntar = True
    while preguntar:
        opcion = int(input('\nSeleccione una opcion: '))
        
        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print ('Opcion no valida, intente de nuevo.')

def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar: ')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado Correctamente')
    except cajeta as identifier:
        print('No existe ese contacto') 

def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea buscar: ')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\nInformacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError) 
    
    # Reiniciar la app
    app()

def mostrar_contacto():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] 

    for archivo in archivos_txt:
        with open (CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())
            # Imprime un separador entre contactos
            print('\r\n') 

def editar_contacto():
    nombre_anterior = input('Nombre del contacto a editar: ')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de los campos
            nombre = input('Agrega el Nuevo Nombre: ')
            telefono = input('Agrega el Nuevo Telefono: ')
            categoria = input('Agrega la Nueva Categoria: ')

            # Instanciar
            contacto = Contacto(nombre, telefono, categoria) 

            # Escribir en el archivo
            archivo.write(f'Nombre: {contacto.nombre}\n')
            archivo.write(f'Telefono: {contacto.telefono}\n')
            archivo.write(f'Categoria: {contacto.categoria}\n')

        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre + EXTENSION) 

        # Mostrar mensaje de exito
        print('\r\nContacto editado Correctamente\r\n')

    else:
        print ('Ese contacto no existe')

     # Reiniciar la app
    app()

def agregar_contacto():
    print ('\nEscribe los datos para agregar el nuevo Contacto\n')
    nombre = input('Nombre del contacto: ')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre)

    if not existe:
          with open(CARPETA + nombre + EXTENSION, 'w') as archivo:

              # Resto de los campos
              telefono = input('Agrega el Telefono: ')
              categoria = input('Categoria contacto: ')

              # Instanciar la clase
              contacto = Contacto(nombre, telefono, categoria)

              # Escribir en el archivo
              archivo.write(f'Nombre: {contacto.nombre}\n')
              archivo.write(f'Telefono: {contacto.telefono}\n')
              archivo.write(f'Categoria: {contacto.categoria}\n')

              # Mostrar un mensaje de exito
              print('\r\nContacto creado correctamente\r\n')
    else:
        print ('Ese contacto ya existe')
    
    # Reiniciar la app
    app()

def mostrar_menu():
    print('\nSeleccione del Menu lo que desea hacer: \n')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta en el caso de que no exista
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
