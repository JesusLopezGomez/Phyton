"""
for i in range (11):
    print(i)
    
for i in range (1, 11):
    print(i)

for i in range (0, 11, 2):
    print(i)
    
for i in range (1, 11, 2):
    print(i)
    
for i in range (-9, 2):
    print(i)
for i in range(0, (num*10)+1, num):
            lim.inf    lim.sup    de cuanto en cuanto
    print(i)
    
"""
"""
num = int(input("Introduzca un número para saber su tabla de multiplicar: "))


for i in range(0, (num*10)+1, num):
    print(i)
"""
"""
variable = 0

while variable < 5:
    print(4-variable)
    variable += 1  
"""
"""
edad = int(input("Introduce tu edad [1-100]: "))

while edad < 1 or edad > 100:
    edad = int(input("Edad errónea, introduce tu edad [1-100]: "))

print(f"Naciste en el año {2022-edad}")
"""
"""
numero=int(input("Enter one number: "))
numerochiquito=numero
while numero<=0:
    numero=int(input("Error enter a number bigger than 0"))
pregunta=input("Do you want to enter more number (Y/N)?")
while pregunta!="Y" and pregunta!="N":
    pregunta=input("Error, Do you want to enter more number (Y/N)?")

while (pregunta)=="Y":
    numero=int(input("Enter one number"))
    pregunta=input("Do you want to enter more number (Y/N)?")
    while numero<=0:
        numero=int(input("Error enter a number bigger than 0"))
    if numero<numerochiquito:
        numerochiquito=numero
        pregunta=input("Do you want to enter more number (Y/N)?")
    while pregunta!="Y" and pregunta!="N":
        pregunta=input("Do you want to enter more number (Y/N)?")
print("El numero mas pequeño es", numerochiquito)
"""

'''
18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite 
inferior es mayor que el superior lo tiene que volver a pedir. 

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:

◦ La suma de los números que están dentro del intervalo (intervalo abierto).

◦ Cuantos números están fuera del intervalo.

◦ Informa si hemos introducido algún número igual a los límites del intervalo.
'''

inf = int(input("Introduce el límite inferior: "))
sup = int(input("Introduce el límite superior: "))

contador = 0
contadorf = 0
suma = 0

while (inf > sup+1): 
    num = int(input("Introduce el límite inferior menor que el superior: "))
    
numero = int(input("Introduce un número: "))

while numero != 0:
    if (numero > inf) and (numero < sup):
        suma += numero
    elif (numero < inf) or (numero > sup):
        contadorf += 1
    else:
        contador += 1
        
    numero = int(input("Introduce un número: "))

print(f"La suma de los números dentro del intervalo es {suma}.")
print(f"Hay {contadorf} números fuera del intervalo.")
print(f"Hay {contador} iguales que los límites.")


