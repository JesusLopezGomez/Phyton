#1
"""
num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

dividendo, divisor = 0, 0
cociente = 0
resto = 0

if num1 == num2:
    cociente = 1
    print(f"El resultado de la división entre {num1} y {num2} es {cociente} y el resto {resto}.")

else:

    if num1 > num2:
        dividendo = num1
        divisor = num2
    
    else: 
        dividendo = num2
        divisor = num1
        
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
        resto = dividendo
print(f"El resultado de la división entre {num1} y {num2} es {cociente} y el resto {resto}.")
"""

#2
"""
Diseñar un programa que pida dos números enteros y nos muestre los siguientes
números que son múltiplos del segundo introducido a partir del primero. Por ejemplo,
si introducimos:
13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77
(a partir de 13 los siguientes 10 múltiplos de 7)

num = int(input("Introduce un número: "))
num1 = int(input("Introduce otro número: "))

for i in range (num, num+num1):
    if (i % num1 == 0):
        num = i
        
        
contador = 0

mensaje = ""

while contador < 10:
    if contador < 9:
        mensaje += str(num)+", "
        
    else: 
        mensaje += str(num)
    num += num1
    contador += 1

print(mensaje)
"""
#3
"""
num = int(input("Introduce un número:"))

while num != 0:
    estado = "positivo"
    n = "par"
    
    if num < 0:
        estado = "negativo"
        
    if num % 2 != 0:
        n = "impar"
        
    print(f"El número {num} es {estado}, {n} y su cuadrado es {num**2}.")
    num = int(input("Introduce un número:"))
print("Se acabó")
"""
#4

"""
Diseña un programa que reciba el tamaño de una secuencia numérica y muestre en
una única línea cada una de las siguientes secuencias. Si se recibe el número 6 se
imprimiría:
a. 1, -5, 25, -125, 625, -3125
b. 1, -1, 0, 1, -1, 0
c. 1, 3, 9, 27, 81, 243

    
tamaño = int(input("Introduzca el tamaño de la secuencia: "))

contador = 0

secuencia_a = 0

secuencia_b = 0 

secuencia_c = 0

mensaje_a = ""

mensaje_b = ""

mensaje_c = ""

while contador < tamaño:
    
    secuencia_a = (-5)**contador
    
    secuencia_b = contador % 3
    if secuencia_b == 0:
        secuencia_b = 1
            
    elif secuencia_b == 1:
        secuencia_b = -1
            
    elif secuencia_b == 2:
        secuencia_b = 0
    
    secuencia_c = 3**contador
    
    contador += 1
    
    if contador < tamaño:
        mensaje_a = mensaje_a + str(secuencia_a) + ","
        mensaje_b= mensaje_b + str(secuencia_b) + ","
        mensaje_c = mensaje_c + str(secuencia_c) + ","
    else:
        mensaje_a = mensaje_a + str(secuencia_a)
        mensaje_b = mensaje_b + str(secuencia_b) 
        mensaje_c = mensaje_c + str(secuencia_c) 
        
print(f"a. {mensaje_a}")
print(f"b. {mensaje_b}")
print(f"c. {mensaje_c}")
"""
#5
"""
5. La secuencia siguiente está definida para el conjunto de los números enteros:

n → n/2 (n es par)
n → 3n + 1 (n es impar)

Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia
de números:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Esta secuencia tiene 10 términos y se cree que cualquier secuencia termina en 1.
Elabora un programa que pida un número n e imprima una cadena con la secuencia
de números hasta llegar a 1.
"""

"""
num = int(input("Introduce un número: "))
num1 = num
mensaje = ""

while num != 1:
    
    if num%2 != 0:
        num = int(num*3 + 1)
        mensaje += str(num) + " --> "
    else: 
        if num == 2:
            num = int(num//2)
            mensaje += str(num)
        else:
            num = int(num//2)
            mensaje += str(num) + " --> "
    

print(str(num1) + " --> " + (mensaje))
"""

#6    

"""

anyo = int(input("Introduce los años que cumple Juan: "))

acomuladorD = 0
acomuladorPuzzle = 0
acomulador = 20
for i in range (1,anyo+1):
    if (i==1):
        acomuladorPuzzle = 1
    elif (i != 1) and (i % 2 != 0):
        acomuladorPuzzle = acomuladorPuzzle * 2 + 1
        
    if (i == 2):
        acomuladorD = 20
    elif (i != 2) and (i % 2 == 0):
        acomuladorD = acomuladorD  + 15
        acomulador = acomulador + acomuladorD 
        
        
print(f"Juan desde que nació ha recibido {acomuladorPuzzle} puzzles y {acomulador} €.") 
"""
    
#7

"""
num = int(input("Introduce un número: "))

for i in range (1,num+1):
    print(i*str(num))
"""

#8a
"""
num = int(input("Introduce un número: "))
for i in range(1,num+1):
    print(str(("* "))*num)
"""   

#8b

"""
    *
   ***
  *****
"""
"""
num = 3

for i in range(1,num*2):
    if i%2 !=0:
        print((num - i)*("  ")+("* ")*i)

"""

num = int(input("¿Cuántos números quieres?"))
n1, n2 = 1,1
contador = 0

while contador < num:
    print(n1)
    resultado = n1 + n2
    n1 = n2
    n2 = resultado
    contador += 1
    


    


