print("Ejercicio 8")

euros, centimos = 0, 0


euros += int(input("Introduce el número de monedas de dos euros que tengas: "))*2
euros += int(input("Introduce el número de monedas de euro que tengas: "))
centimos += int(input("Introduce el número de monedas de 50 centimos que tengas: "))*50
centimos += int(input("Introduce el número de monedas de 20 centimos que tengas: "))*20
centimos += int(input("Introduce el número de monedas de 10 centimos que tengas: "))*10
centimos += int(input("Introduce el número de monedas de 5 centimos que tengas: "))*5
centimos += int(input("Introduce el número de monedas de 2 centimos que tengas: "))*2
centimos += int(input("Introduce el número de monedas de 1 centimo que tengas: "))

print("La suma del dinero introducido es de: " + str(float(int(euros%100) + (centimos/100))) + "€" )


