def paso_por_referencia(objeto):
    objeto.nuevo_atributo = 'nuevo atributo'

def paso_por_valor(algo):
    print(algo)

class Prueba:
    pass

prueba1 = Prueba()

paso_por_referencia(prueba1)
print(prueba1.nuevo_atributo)