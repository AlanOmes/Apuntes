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
print (f'Hola, {nombre}, las siguientes preguntas se deben responder por SI o por NO: ')


pregunta_1 = input ('Chuty es el mejor freestyler del mundo? \r\n ')
correcta = 'SI'
incorrecta = 'NO' 
puntaje = 0

if pregunta_1 == correcta:
    print ('Respuesta correcta')
elif pregunta_1 == 'si':
    print ('Respuesta correcta')
elif pregunta_1 == 'Si':
    print ('Respuesta correcta')
elif correcta == puntaje + 1:
    print ('Ha sumado 1 punto')
elif pregunta_1 == incorrecta:
    print ('Respuesta incorrecta')
elif pregunta_1 == 'No':
    print ('Respuesta incorrecta')
elif pregunta_1 == 'no':
    print ('Respuesta incorrecta')
else:
    print ('Por favor, solo responda con "SI o "NO"')


pregunta_2 = input ('Bnet es mejor que Gazir? \r\n')
correcta = 'NO'
incorrecta = 'SI'

if pregunta_2 == correcta:
    print ('Respuesta correcta')
elif pregunta_2 == 'No':
    print ('Respuesta correcta')
elif pregunta_2 == 'no':
    print ('Respuesta correcta')
elif pregunta_2 == incorrecta:
    print ('Respuesta incorrecta')
elif pregunta_2 == 'Si':
    print ('Respuesta incorrecta')
elif pregunta_2 == 'si':
    print ('Respuesta incorrecta')
else:
    print ('Por favor, solo responda con "SI" o "NO"')


pregunta_3 = input ('Juli está extremadamente buena? \r\n')
correcta = 'SI'
incorrecta = 'NO'

if pregunta_3 == correcta:
    print ('Respuesta correcta')
elif pregunta_3 == 'Si':
    print ('Respuesta correcta')
elif pregunta_3 == 'si':
    print ('Respuesta correcta')
elif pregunta_3 == incorrecta:
    print ('Le recomendamos comprarse anteojos')
elif pregunta_3 == 'No':
    print ('Le recomendamos comprarse anteojos')
elif pregunta_3 == 'no':
    print ('Le recomendamos comprarse anteojos')
else:
    print ('Por favor, solo responda con "SI o "NO"')

