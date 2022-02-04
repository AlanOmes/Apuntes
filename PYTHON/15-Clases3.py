class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio
        
        
    def mostrar_informacion(self):
        print (f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')


# Instanciar la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)

print (restaurant.precio)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas Python', 'Comida Casual', 20)
print(restaurant2.precio)
restaurant2.mostrar_informacion()

