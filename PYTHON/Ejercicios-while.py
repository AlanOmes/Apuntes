# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste 
# exactamente sí (en minúsculas y con tilde)

'''

pregunta = '¿Desea continuar con el programa? \r\n'
preguntar = True

while preguntar:
    respuesta = input (pregunta)
    if respuesta == 'sí':
        print ()
    else:
        preguntar = False
        print ('¡Hasta la vista!')

'''

# Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta exactamente
# SI (en mayúsculas y sin tilde)

'''

pregunta = '¿Desea terminar el programa? \r\n'
preguntar = True 

while preguntar:
    respuesta = input (pregunta)
    if respuesta == 'SI':
        preguntar = False
        print ('¡Hasta la vista!')

'''

# Escriba un programa que pregunte una y otra vez si desea terminar el programa, siempre que se conteste exactamente
# N (en mayúsculas)

'''

pregunta = 'Desea terminar el programa? \r\n'
preguntar = True

while preguntar:
    respuesta = input (pregunta)
    if respuesta == 'N':
        print ()
    else:
        preguntar = False
        print ('¡Hasta la vista!')

'''

# Escriba un programa que pregunte una y otra vez si desea continuar el programa, salvo si se contesta exactamente
# no (en minúsculas)

'''

pregunta = 'Desea continuar con el programa? \r\n'
preguntar = True

while preguntar:
    respuesta = input (pregunta)
    if respuesta == 'no':
        preguntar = False
        print ('¡Hasta la vista!')

'''

# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste 
# S o s (en mayúsculas o en minúsculas)

'''

pregunta = 'Desea continuar con el programa? \r\n'
preguntar = True

while preguntar:
    respuesta = input(pregunta)
    if respuesta == 'S' or respuesta == 's':
        print ()
    else:
        preguntar = False
        print ('¡Hasta la vista!')

'''

# Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta S o s 
# (en mayúsculas o en minúsculas)

'''

pregunta = 'Desea terminar el programa? \r\n'
preguntar = True

while preguntar:
    respuesta = input(pregunta)
    if respuesta == 's' or respuesta == 'S':
        preguntar = False
        print ('¡Hasta la vista!')

'''

# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a 
# solicitar hasta que las dos contraseñas coincidan

'''

pregunta = 'Ingrese su contraseña: \r\n'
pregunta_2 = 'Ingrese su contraseña nuevamente: \r\n'
preguntar = True

while preguntar:
    respuesta = input (pregunta)
    respuesta_2 = input (pregunta_2)
    if respuesta == respuesta_2:
        preguntar = False
        print ('Contraseña confirmada. ¡Hasta la vista!')
    else:
        print ('Las contraseñas no coinciden. Inténtelo nuevamente.')

'''

# Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad
# de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se
# irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las 
# cantidades sean positivas.

'''

pregunta = '¿Cuántos euros quiere ahorrar? \r\n'
pregunta_2 = '¿Cuántos euros quiere ingresar en la cuenta? \r\n'
objetivo = 0
preguntar = True

objetivo_final = int (input (pregunta))

while preguntar:
    ingresar = int (input(pregunta_2))
    objetivo = objetivo + ingresar
    if objetivo >= objetivo_final:
        preguntar = False
        print (f'¡Objetivo conseguido! Ha ahorrado {objetivo} euros.')
    
'''

# Escriba un programa que mejore la simulación de la hucha del ejercicio anterior, no permitiendo que se 
# escriban cantidades negativas.

'''

pregunta = '¿Cuántos euros quiere ahorrar? \r\n'
pregunta_2 = '¿Cuántos euros quiere ingresar en la cuenta? \r\n'
objetivo = 0
preguntar = True

objetivo_final = int (input (pregunta))

while preguntar:
    ingresar = int (input(pregunta_2))
    objetivo = objetivo + ingresar
    if objetivo >= objetivo_final:
        preguntar = False
        print (f'¡Objetivo conseguido! Ha ahorrado {objetivo} euros.')
    elif ingresar < 0:
        ingresar = ingresar * (-1)
        objetivo = objetivo + ingresar
        print ('Por favor, escriba una cantidad positiva.')

'''

# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a
# solicitar, hasta que las dos contraseñas coincidan con un límite de 3 peticiones.
        
pregunta = 'Escriba su contraseña: \r\n'
pregunta_2 = 'Escriba de nuevo su contraseña: \r\n'
intentos = 0
preguntar = True 

contraseña = input (pregunta)
print ('Tiene 3 intentos para confirmar su contraseña.')

while preguntar:
    confirmar = input (pregunta_2)
    if confirmar == contraseña:
        preguntar = False
        print ('Contraseña confirmada. ¡Hasta la vista!')
    else:
        intentos = intentos + 1
        print ('Las contraseñas no coinciden. Inténtelo de nuevo.')
        if intentos > 2:
                preguntar = False
                print ('Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!')
    

        

    
    




        
        
         
       
       
       
       
        
        
    
    
    
    
    
    
    