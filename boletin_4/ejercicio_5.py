print("Ejercicio 5")

num1 = int(input("Inserta un número: "))
num2 = int(input("Inserta otro número: "))

if (num1 - num2) > 0:
    print(f"La distancia entre ellos es de: {num1 - num2}" )
    
elif (num2 - num1) > 0:
    print(f"La distancia entre ellos es de: {num2 - num1}")
    
else:
    print("¡Error!")