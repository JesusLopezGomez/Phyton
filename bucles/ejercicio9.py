      
num = int(input("Introduce un número mayor que 0: "))
suma = 0

for i in range(1, num):
    if (num%i == 0):
        suma += i

while num < 0:
    num = int(input("El número introducido no es correcto, inténtalo de nuevo: "))

if (suma == num):
    print(f"El {num} es perfecto.")
    
else:
    print(f"El {num} no es perfecto.")


        
    