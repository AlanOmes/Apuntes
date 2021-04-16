# Pedir datos al usuario

'''


nombre = input('Ingrese su nombre: ') # Se le puede agregar \r\n si quiero hacer un salto de línea -> que el nombre se escriba abajo
print (f'Hola {nombre}')

# Leer datos que serán números

edad = int (input ('Cuál es tu edad? '))

if edad >= 18:
    print ('Ya puedes votar')
else:
    print ('Aún no puedes votar')

'''

# Mezclarlo con operadores

'''

numero = int (input ('Agrega un número y te diré si es par o no: \r\n'))



if numero % 2 == 0:
    print (f'El número {numero} es par')
else:
    print (f'El número {numero} es impar')

'''

# RETO

# Realiza un examen con 3 preguntas que tu desees, el usuario debe responder "SI" o "NO", y al final otorgarle
# una calificación (la calificación se logra con una variable que inicia en 0 y por cada respuesta correcta 
# incrementa en 1)

nombre = input ('Ingrese su nombre: ')
print (f'Hola, {nombre}, las siguientes preguntas se deben responder por SI o por NO ')


pregunta_1 = input ('Chuty es el mejor freestyler del mundo? ')
correcta = 
