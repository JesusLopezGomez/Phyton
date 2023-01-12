import math

print("Ejercicio 7")

num = int(input("Introduzca un número:"))

print(("La raiz cuadrada del número introducido es de: ") + str(float(int(math.sqrt(num)))))

def raiz_cubica(num):
    return num**(1. / 3.)

print(("La raiz cúbica del número introducido es de: ") + str(float(int(raiz_cubica(num)))))