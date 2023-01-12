
num = int(input("Inserta un número mayor que 0: ")) 

while num <= 0:
    num = int(input("El número no es correcto, inténtalo de nuevo: ")) 

for i in range(1, num+1):
    print(f"{num} + {i} = {i+num}")


