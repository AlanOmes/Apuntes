# Teoría: condiciones

# El if se usa cuando quiero ejecutar 0 o 1 vez algo

numero = int(input("Ingresa un número:"))

if numero > 5 and numero < 10:
    print("Es mayor que cinco y menor que diez")
elif numero > 5 and numero > 10:
    print("Es mayor que cinco y mayor que diez")
elif numero == 10:
    print("Es igual a 10")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor que 5 y 10")     



