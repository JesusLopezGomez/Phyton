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
