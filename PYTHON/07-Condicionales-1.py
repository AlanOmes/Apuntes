# Revisar si una condición es mayor a

'''

balance = 500
if balance > 500:
    print ('Puedes pagar')

'''

# Else -> Si una condición es evaluada como verdadera, se ejecutará un código
# Pero algunas veces deseas tener otra acción que se realice en caso de que la condición no se cumpla

'''

balance = 0
if balance > 0:
    print ('Puedes pagar')
else:
    print ('No tienes saldo')

'''

# Likes

'''

likes = 200
if likes >= 200:
    print ('Excelente, tienes 200 likes')
else:
    print ('Casi llegas a 200 likes')

'''

# If con texto

'''

lenguaje = 'Python'
if not lenguaje == 'Python': # Not: nega la condición -> si es true, negado se hace false
    print ('Excelente decisión')
    

'''

# Evaluar un Boolean

'''

usuario_autenticado = True

if usuario_autenticado: # Cuando se evalúa un Booleano no es necesario añadir el " == ", revisa automáticamente si es verdadero o falso
    print ('Acceso al sistema')
else:
    print('Debes iniciar sesión')

'''

# Evaluar un elemento de una lista

'''

lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'PHP']

if 'PHP' in lenguajes:
    print('PHP Si existe')
else:
    print ('No, no está en la lista')

'''

# If Anidados 

'''

usuario_autenticado = True
usuario_admin = True

if usuario_autenticado: 
    if usuario_admin:
        print ('ACCESO TOTAL')
    else:
        print ('Acceso al sistema')
else:
    print('Debes iniciar sesión')

'''