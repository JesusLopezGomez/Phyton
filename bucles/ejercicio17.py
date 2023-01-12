'''
17. Escribir un programa que imprima todos los números pares entre dos números que se le 
pidan al usuario
'''

num = int(input("Introduce un número: "))
num1 = int(input("Introduce otro número: "))

for i in range (num, num1+1):
    if (i%2 == 0):
        print(i)