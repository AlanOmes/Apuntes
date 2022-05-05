'''

import math # Importo todos los métodos de math (también puede ser from math import *)
print(math.ceil(2.7)) # Redondea para arriba -> 3
print(math.floor(2.7)) # Redondea para abajo -> 2

from math import ceil, floor # Importo solamente los metodos que necesito

print(ceil(2.7))
print(floor(2.7)) 

'''



import mi_modulo # Carga todo lo que esté dentro del archivo

print(mi_modulo.variable) 

from mi_modulo import variable, sumar, Persona # Cargo solamente lo que necesito usar  

print(variable)

print(sumar(1, 2))

p1 = Persona()

print(p1.nombre)

# DATO -> Si el archivo que quiero cargar está dentro de una carpeta, debo poner:
# from nombreCarpeta.nombreArchivo import variable, sumar, Persona