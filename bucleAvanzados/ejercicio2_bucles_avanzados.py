#2
"""
Diseñar un programa que pida dos números enteros y nos muestre los siguientes
números que son múltiplos del segundo introducido a partir del primero. Por ejemplo,
si introducimos:
13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77
(a partir de 13 los siguientes 10 múltiplos de 7)
"""
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



