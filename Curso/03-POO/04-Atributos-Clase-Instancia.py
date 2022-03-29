# Los atributos de clase son atributos compartidos por todas las instancias de esa clase.

class Prueba():

    atributo1 = 'algo'
    atributo2 = 'otra cosa'

a = Prueba()
b = Prueba()

# Los atributos de instancia, por el contrario, son únicos para cada uno de los objetos pertenecientes a dicha clase.

a.otro_atributo = 'otro atributo'

print(a.otro_atributo)
print(b.otro_atributo)

