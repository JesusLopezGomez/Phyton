
print("Ejercicio 9")

base = int(input("Introduzca un número base: "))
exp = int(input("Introduzca un número exponiente de base: "))

if (exp > 0):
    print("La potencia de los números introducido es: " + str(int(base ** exp)))
    
elif (exp == 0):
    print("La potencia de los números introducido es: " + str(int(base ** exp)))
    
elif (exp < 0):
    print("La potencia de los números introducido es: " + str(int(1/(base ** exp))))
