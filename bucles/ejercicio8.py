
num = int(input("Introduce un número: "))
sino =(input("¿Quieres ingresar más número (y/n): "))
numpequeño = num
while (sino == "y"):
        num = int(input("Introduce un número: "))
        if (num < numpequeño):
                numpequeño = num
        sino =(input("¿Quieres ingresar más número (y/n): "))    
    
print(f"El número más pequeño es {numpequeño}")



    
    
