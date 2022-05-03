from copy import copy # Se utiiza deecopy si es una copia más profunda

class Prueba:
    pass

prueba1 = Prueba()
prueba2 = copy(prueba1)

prueba1.atributo = 'algo'
prueba2.atributo = 'otra cosa'

print(prueba1.atributo)
print(prueba2.atributo)