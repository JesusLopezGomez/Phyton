
print("Ejercicio 12")

tipouva = input("Introduzca el tipo de uva que quiere (a/b): ")
tamannouva = int(input("Introduzca el tamaño de uva que quiere (1/2): "))

kuva = float(2)

if (tipouva == "a" and tamannouva == 1):
    print("El precio final del kilo de uva de tipo a y tamaño 1, es de: " + str(float(kuva + 0.20)) + "€" )
    print("La ganancia obtenida es de 0.20 centimos")
    
elif (tipouva == "a" and tamannouva == 2):
    print("El precio final del kilo de uva de tipo a y tamaño 2, es de: " + str(float(kuva + 0.30)) + " €" )
    print("La ganancia obtenida es de 0.30 centimos")
    
elif(tipouva == "b" and tamannouva == 1):
    print("El precio final del kilo de uva de tipo b y tamaño 1, es de: " + str(float(kuva - 0.30)) + "€")
    print("La ganancia obtenida es de -0.30 centimos")
    
elif (tipouva == "b" and tamannouva == 2):
    print("El precio final del kilo de uva de tipo b y tamaño 2, es de: " + str(float(kuva - 0.50)) + "€")
    print("La ganancia obtenida es de -0.50 centimos")


    