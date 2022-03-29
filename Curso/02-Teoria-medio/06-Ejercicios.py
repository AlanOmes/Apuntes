# Ejercicio 1: Dado un número natural x, mostrar su último dígito.

# Concepto matemático 

'''

num = int(input('Ingrese un número natural: '))
ult_digito = num % 10

if num >= 0:
    print(f'El último dígito es {ult_digito}')
else:
    print('Oops! Ingresa un número natural.')

'''

# Estilo Python

'''

num = input('Ingrese un número natural: ')

if num.isnumeric(): # Pregunta si es int
    print(f'El último dígito es {num[-1]}')
else:
    print('Oops! Ingresa un número natural.')

'''

# Ejercicio 2: Dado un número natural x, contar la cantidad de dígitos que posee.

'''

# Concepto matemático
num = int(input('Ingresar un número natural: '))
c = 0

if 0 <= num < 10:
    print('La cantidad de dígitos son: 1')
else:
    while num > 0:
        c += 1
        num = num // 10
    print(f'La cantidad de dígitos son: {c}')

'''

'''

# Python
num = input('Ingrese un número natural: ')

if num.isnumeric():
    print(f'La cantidad de dígitos son: {len(num)}')
else:
    print('Oops! Ingresa un número natural.')

'''

# Ejercicio 3: Dado un número natural x, contar la cantidad de dígitos pares e impares que posee.

'''

num = input('Ingrese un número natural: ')
pares = 0
impares = 0

for digito in num:
    if int(digito) % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'La cantidad de dígitos pares son: {pares}')
print(f'La cantidad de dígitos impares son: {impares}')

'''

# Ejercicio 4: Dado un número natural x, sumar todos sus dígitos. Mostrar la suma obtenida.

'''

num = int(input('Ingrese un número natural: '))
suma = 0

while num > 0:
    suma += num % 10
    num = num // 10

print (f'La suma de todos los dígitos es {suma}')

'''

# Ejercicio 5: Dado un número natural x, determinar si es capicúa.

'''

num = int(input('Ingrese un número natural: '))
num = str(num)

if num == num[::-1]:
    print('El número es capicúa.')
else:
    print('El número no es capicúa.')

'''

# Ejercicio 6: 