
num = int(input("¿Cuántos números quieres ingresar?: "))
contador = 0

while (num < 0):
    num = int(input("El número no es válido, debe ser mayor que 0: "))
    
for i in range (num):
    num1 = int(input("Introduzca un número mayor que 0: "))
    contador += num1

print(f"La media de los números es {contador/num}")


