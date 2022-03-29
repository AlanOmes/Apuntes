class Persona:
    def __init__(self, color_de_pelo, altura, tipo_de_voz):
        self.color_de_pelo = color_de_pelo
        self.altura = altura
        self.tipo_de_voz = tipo_de_voz
    
    def obtener_color_de_pelo(self):
        return self.color_de_pelo

julian = Persona(color_de_pelo = "oscuro", altura = 1.80, tipo_de_voz = "grave")
ana = Persona("rojo", 1.72, "aguda")

print(julian.color_de_pelo)
print(ana.obtener_color_de_pelo())

