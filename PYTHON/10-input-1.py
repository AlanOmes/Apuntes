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


# pregunta_1 = input ('Chuty es el mejor freestyler del mundo? \r\n ')
puntaje = 0 # SE INCREMENTA EN 1 CUANDO LA RESPUESTA ES CORRECTA (por pregunta)

'''


if pregunta_1 == correcta:
    puntaje = puntaje + 1 
    print ('Respuesta correcta')
elif pregunta_1 == 'si':
    puntaje = puntaje + 1
    print ('Respuesta correcta')
elif pregunta_1 == 'Si':
    puntaje = puntaje + 1
    print ('Respuesta correcta')
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

creo que lo intente con or igual y no funciono 

if pregunta_2 == correcta:
    puntaje = puntaje + 1
    print ('Respuesta correcta')
elif pregunta_2 == 'No':
    puntaje = puntaje + 1
    print ('Respuesta correcta')
elif pregunta_2 == 'no':
    puntaje = puntaje + 1
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

if pregunta_3 == 'SI':
    puntaje = puntaje + 1
    print ('Respuesta correcta')
elif pregunta_3 == 'Si':
    puntaje = puntaje + 1
    print ('Respuesta correcta')
elif pregunta_3 == 'si':
    puntaje = puntaje + 1
    print ('Respuesta correcta')
elif pregunta_3 == incorrecta:
    print ('Le recomendamos comprarse anteojos')
elif pregunta_3 == 'No':
    print ('Le recomendamos comprarse anteojos')
elif pregunta_3 == 'no':
    print ('Le recomendamos comprarse anteojos')
else:
    print ('Por favor, solo responda con "SI o "NO"')

if puntaje == 3:
    ('Felicitaciones, aprobó el exámen')
elif puntaje == 2:
    ('Felicitaciones, aprobó el exámen')
else:
    print ('Retirate burro de mierda, puto')

'''

pregunta_4 = input ('Juli le tiene unas ganas inexplicables a Alan? \r\n')


if pregunta_4 == 'Si' or pregunta_4 ==' SI' or pregunta_4 == 'si':
    puntaje = puntaje + 1
    print ('Respuesta correcta')
else:
    print ('Mirá si no le va a tener ganas...')

if puntaje == 1:
    print (f'Felicitaciones, aprobó el exámen, {nombre}' )
else: 
    print ('Puto') 

