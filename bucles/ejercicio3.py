

numeros = int(input("¿Cuantos números deseas introducir?: "))

while numeros <= 0:
    numeros = int(input("Error introduce un número mayor que 0: "))

for i in range (numeros):
    numeros = int(input("Introduce los números: "))
    while numeros <= 0:
        numeros = int(input("Error introduce un número mayor que 0: "))
        if (0 <(numeros%2 == 0)):
            print(f"El {numeros} es par")
        elif (0 <(numeros%2 == 1)):
            print(f"El {numeros} es impar")



    

    