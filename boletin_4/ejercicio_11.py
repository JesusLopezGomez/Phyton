
print("Ejercicio 11")

año = int(input("Introduce un año y te diré si es bisiesto o no ^^: "))

if (año%4 == 0):
    print("El año introducido es bisiesto")
    
elif (año%100 >= 1):
    print("El año introducido no es bisiesto")
    
elif (año%400 == 0):
    print("El año introducido es bisiesto")
