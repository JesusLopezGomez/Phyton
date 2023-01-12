"""
21. Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
números primos que queremos mostrar.
"""

#cantidad = int(input("Introduce la cantidad de números primos que quieres saber: "))

for i in range (1,101):
    if (i%1 == 0) and (i%i == 0) and (i%i+1 != 0):
        print(i)