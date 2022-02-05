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
            print ('Editar contacto')
            preguntar = False
        elif opcion == 3:
            print ('Ver contactos')
            preguntar = False
        elif opcion == 4:
            print ('Buscar contacto')
            preguntar = False
        elif opcion == 5:
            print ('Eliminar contacto')
            preguntar = False
        else:
            print ('Opcion no valida, intente de nuevo.')

def agregar_contacto():
    print ('\nEscribe los datos para agregar el nuevo Contacto\n')
    nombre = input('Nombre del contacto: ')

    # Revisar si el archivo ya existe antes de crearlo
    existe = os.path.isfile(CARPETA + nombre + EXTENSION)

    if not existe:
          with open(CARPETA + nombre + EXTENSION, 'w') as archivo:
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
    
app()
