import math
print("Ejercicio 6")


x1 = int(input("Introduzca el valor númerico de x1: "))
y1 = int(input("Introduzca el valor númerico de y1: "))
x2 = int(input("Introduzca el valor númerico de x2: "))
y2 = int(input("Introduzca el valor númerico de y2: "))

distancia = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))

print(f"La distancia entres los puntos es {distancia}")