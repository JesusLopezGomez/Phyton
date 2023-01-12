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
