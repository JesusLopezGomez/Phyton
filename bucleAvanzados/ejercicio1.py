
"""
num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

resto = 0
cociente = 0

if num1 > num2:
    divisor = num2
    dividendo = num1 
    
else:
    divisor = num1
    dividendo = num2
    
while dividendo >= divisor: 
    dividendo -= divisor 
    cociente += 1
    resto = dividendo
    
print(f"El cociente de la división es; {cociente} y el resto es; {resto}. ")

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
    
    
    
    