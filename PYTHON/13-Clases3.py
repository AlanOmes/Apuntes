class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.__precio = precio # Default: Public 
        
    def mostrar_informacion(self):
        print (f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
    
    # GETTERS Y SETTERS -- Get = Obtiene un valor, Set: Agrega o modifica un valor
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio



# Instanciar la clase

restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
# restaurant.__precio = 80 # No sera posible modificarlo con PRIVATE __
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print (precio)

restaurant2 = Restaurant('Hamburguesas Python', 'Comida Casual', 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()


# Tipos de Default:

# Public: self.precio (el atributo se puede modificar en cualquier parte del programa)
# PROTECTED: self.__precio (el atributo se puede modificar en la misma clase)
# PRIVATE: self.__precio (el atributo solo se puede modificar con los metodos GETTERS y SETTERS)
    