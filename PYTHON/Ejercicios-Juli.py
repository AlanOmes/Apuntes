# Crear un programa que pida al usuario ingresar un número infinitamente, y que cuando ponga -1, deje de pedir
# e informe cuántos "5" puso en total.

pregunta = 'Ingrese un número: \r\n' 
pregunta += '(Escriba "-1" para finalizar) \r\n'
preguntar = True 
cant_5 = 0
cant_par = 0


while preguntar:
    numero = int (input (pregunta))

    if numero == 5:
        cant_5 = cant_5 + 1
    elif numero % 2 == 0:
        cant_par = cant_par + 1
    elif numero == 11:
        for i in range (11):
            print ('Juli es lo más ♥')
    else:
        numero = int (numero)
        if numero == -1:
            preguntar = False 
            print ('Cantidad de veces que escribió el numero 5: ', cant_5)
            print ('Cantidad de veces que escribió un número par: ', cant_par)
            for i in range (cant_5):
                print ('Te quiero')

