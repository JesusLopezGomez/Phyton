
print("Ejercicio 10")

a = int(input("Introduce la dimesión del lado A: "))
b = int(input("Introduce la dimesión del lado B: "))
c = int(input("Introduce la dimesión del lado C: "))

if ((a**2 + b**2) == c**2 ):
    print("Los lados introducidos coinciden con el triángulo rectangulo.")

elif (a == b ==c):
    print("Los lado introducidos coinciden con el triángulo equilátero.")

elif (a == b or a == c or c == b):
    print("Los lado introducidos coinciden con el triángulo isósceles.")
    
else: 
    print("Los lado introducidos coinciden con el triángulo escaleno.")