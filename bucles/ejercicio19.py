"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia.
"""

base = int(input("Introduce un número entero positivo base: "))
exp = int(input("Introduce un número entero positivo exponente: "))

resultado = 1

for i in range(exp):
    resultado = base*resultado

print(f"El resultado de la potencia introducida es: {resultado}")