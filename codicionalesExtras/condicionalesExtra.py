"""
#Ejercicio 1
 Escribe el código de un programa que reciba un número de nota de 0 a 100 y nos
informe de las calificaciones en el siguiente formato:
90-100, Sobresaliente
70-89, Notable
60-69, Bien
50-59, Suficiente
0-49, Suspenso



nota = int(input("Introduce tu nota(En el siguiente formato, 5 = 50): "))

if (nota <= 49) and (nota >= 0):
    print(f"Has sacado un {nota}, suspenso.")

elif (nota >= 50) and (nota <= 59):
    print(f"Has sacado un {nota}, suficiente.")

elif (nota >= 60) and (nota <= 69):
    print(f"Has sacado un {nota}, bien.")

elif (nota >= 70) and (nota <= 89):
    print(f"Has sacado un {nota}, notable.")

elif (nota >= 90) and (nota <= 100):
    print(f"Has sacado un {nota}, sobresaliente.")



Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio
(Norte/Sur) e indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21
diciembre), Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21
diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio).

#Ejercicio 2

hemisferio = input("Introduce el hemisferio: ").lower()
mes = input("Introduce el mes: ").lower()
dia = int(input("Introduce el día: "))




if hemisferio =="norte":
    #Otoño
    if (mes == "diciembre"):
        if (dia < 21):
            print("Estás en la estación de Otoño.")
    
    elif (mes == "septiembre"):
        if (dia > 23):
            print("Estás en la estación de Otoño.")
    
    elif (mes == "septiembre") or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Otoño.")
    
    #Invierno        
    elif (mes == "marzo"):
        if (dia < 21):
            print("Estás en la estación de Invierno.")
    
    elif (mes == "diciembre"):
        if (dia > 21):
            print("Estás en la estación de Invierno.")
            
    elif (mes == "diciembre") or (mes == "enero") or (mes == "febrero") or (mes =="marzo"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Invierno.")
    
    #Primavera
    elif (mes == "junio"):
        if (dia < 21):
            print("Estás en la estación de Primavera.")
    
    elif (mes == "marzo"):
        if (dia > 21):
            print("Estás en la estación de Primavera.")
            
    elif (mes == "marzo") or (mes == "abril") or (mes == "mayo") or (mes =="junio"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Primavera.")
    
    #Verano
    elif (mes == "junio"):
        if (dia > 21):
            print("Estás en la estación de Verano.")
    
    elif (mes == "septiembre"):
        if (dia < 23):
            print("Estás en la estación de Verano.")
            
    elif (mes == "junio") or (mes == "julio") or (mes == "agosto") or (mes =="septiembre"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Verano.")
            
if hemisferio =="sur":
    #Otoño
    if (mes == "junio"):
        if (dia < 21):
            print("Estás en la estación de Otoño.")
    
    elif (mes == "marzo"):
        if (dia > 21):
            print("Estás en la estación de Otoño.")
    
    elif (mes == "marzo") or (mes == "abril") or (mes == "mayo") or (mes == "junio"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Otoño.")
    
    #Invierno        
    elif (mes == "septiembre"):
        if (dia < 23):
            print("Estás en la estación de Invierno.")
    
    elif (mes == "junio"):
        if (dia > 21):
            print("Estás en la estación de Invierno.")
            
    elif (mes == "junio") or (mes == "julio") or (mes == "agosto") or (mes =="septiembre"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Invierno.")
    
    #Primavera
    elif (mes == "diciembre"):
        if (dia < 21):
            print("Estás en la estación de Primavera.")
    
    elif (mes == "septiembre"):
        if (dia > 23):
            print("Estás en la estación de Primavera.")
            
    elif (mes == "septiembre") or (mes == "octubre") or (mes == "noviembre") or (mes =="diciembre"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Primavera.")
    
    #Verano
    elif (mes == "diciembre"):
        if (dia > 21):
            print("Estás en la estación de Verano.")
    
    elif (mes == "marzo"):
        if (dia < 21):
            print("Estás en la estación de Verano.")
            
    elif (mes == "diciembre") or (mes == "enero") or (mes == "febrero") or (mes =="marzo"):
        if (dia >= 1) and (dia <= 31):
            print("Estás en la estación de Verano.")
"""

#Ejercicio 3
"""
Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva
cuántos días han transcurrido desde el 1 de enero de ese mismo año (considera que
puede tratarse de un año bisiesto).
"""

fecha = input("Introduce una fecha (dd-mm-yyyy): ")

dia = int(fecha [0:2])
mes = int(fecha [3:5])
año = int(fecha [6:10])

bisiesto = (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0)

diasTotales = 0

if (mes ==  1) and (1 <= dia <= 31):
    diasTotales = dia

elif (mes == 2) and (1 <= dia) and ((bisiesto and dia <= 29) or (not bisiesto and dia <= 28)):
    diasTotales = 31 + dia

else: 
    print("La fecha introducida no es correcta.")


print(diasTotales)




