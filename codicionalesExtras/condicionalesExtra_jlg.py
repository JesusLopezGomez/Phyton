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


#Ejercicio 3

Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva
cuántos días han transcurrido desde el 1 de enero de ese mismo año (considera que
puede tratarse de un año bisiesto).


fecha = input("Introduce una fecha (dd-mm-yyyy): ")

dia = int(fecha [0:2])
mes = int(fecha [3:5])
año = int(fecha [6:10])

bisiesto = (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0)

diasTotales = 0

if (bisiesto == True):
    if (mes ==  1) and (1 <= dia <= 31):
        diasTotales = dia
    
    elif (mes == 2) and (1 <= dia <= 29):
        diasTotales = 31 + dia
    
    elif (mes == 3) and (1 <= dia <= 31):
        diasTotales = 31 + 29 + dia
    
    elif (mes == 4) and (1 <= dia <= 30):
        diasTotales = 31 + 29 + 31 + dia
    
    elif (mes == 5) and (1 <= dia <= 30):
        diasTotales = 31 + 29 + 31 + 30 + dia

    elif (mes == 6) and (1 <= dia <= 31):
        diasTotales = 31 + 29 + 31 + 30 + 30 + dia
        
    elif (mes == 7) and (1 <= dia <= 31):
        diasTotales = 31 + 29 + 31 + 30 + 30 + 31 + dia
        
    elif (mes == 8) and (1 <= dia <= 31):
        diasTotales = 31 + 29 + 31 + 30 + 30 + 31 + 31 + dia
        
    elif (mes == 9) and (1 <= dia <= 30):
        diasTotales = 31 + 29 + 31 + 30 + 30 + 31 + 31 + 31 + dia
        
    elif (mes == 10) and (1 <= dia <= 31):
        diasTotales = 31 + 29 + 31 + 30 + 30 + 31 + 31 + 31 + 30 + dia
        
    elif (mes == 11) and (1 <= dia <= 30):
        diasTotales = 31 + 29 + 31 + 30 + 30 + 31 + 31 + 31 + 30 + 31 + dia

    elif (mes == 12) and (1 <= dia <= 31):
        diasTotales = 31 + 29 + 31 + 30 + 30 + 31 + 31 + 31 + 30 + 31 + 30 + dia
    

if (bisiesto == False):
    if (mes ==  1) and (1 <= dia <= 31):
        diasTotales = dia
    
    elif (mes == 2) and (1 <= dia <= 28):
        diasTotales = 31 + dia
    
    elif (mes == 3) and (1 <= dia <= 31):
        diasTotales = 31 + 28 + dia
    
    elif (mes == 4) and (1 <= dia <= 30):
        diasTotales = 31 + 28 + 31 + dia
    
    elif (mes == 5) and (1 <= dia <= 30):
        diasTotales = 31 + 28 + 31 + 30 + dia

    elif (mes == 6) and (1 <= dia <= 31):
        diasTotales = 31 + 28 + 31 + 30 + 30 + dia
        
    elif (mes == 7) and (1 <= dia <= 31):
        diasTotales = 31 + 28 + 31 + 30 + 30 + 31 + dia
        
    elif (mes == 8) and (1 <= dia <= 31):
        diasTotales = 31 + 28 + 31 + 30 + 30 + 31 + 31 + dia
        
    elif (mes == 9) and (1 <= dia <= 30):
        diasTotales = 31 + 28 + 31 + 30 + 30 + 31 + 31 + 31 + dia
        
    elif (mes == 10) and (1 <= dia <= 31):
        diasTotales = 31 + 28 + 31 + 30 + 30 + 31 + 31 + 31 + 30 + dia
        
    elif (mes == 11) and (1 <= dia <= 30):
        diasTotales = 31 + 28 + 31 + 30 + 30 + 31 + 31 + 31 + 30 + 31 + dia

    elif (mes == 12) and (1 <= dia <= 31):
        diasTotales = 31 + 28 + 31 + 30 + 30 + 31 + 31 + 31 + 30 + 31 + 30 + dia


print(diasTotales)


#Ejercicio 4


grupos = input("Introduce dos grupos sanguíneos (ej: A y B): ").lower()

recibe_a = "a y 0"
dona_a = "a y ab"

recibe_b = "b y 0"
dona_b = "b y ab"

recibe_ab = "a b ab y 0"
dona_ab = "ab"

recibe_0 = "0"
dona_0 = "a b ab y 0"

if (grupos == "a y b") or (grupos == "b y a"):
    print("Los grupos introducidos no son compatibles.")

    
elif (grupos == "a y ab") or (grupos == "ab y a"):
    print("Los grupos introducidos son compatibles, a puede donar a; ab")
    
    
elif (grupos == "b y ab") or (grupos == "ab y b"):
    print("Los grupos introducidos son compatibles, b puede donar a; ab.")

elif (grupos == "0 y a") or (grupos == "a y 0"):
    print("Los grupos introducidos son compatibles, 0 puede donar a; a.")

elif (grupos == "0 y ab") or (grupos == "ab y 0"):
    print("Los grupos introducidos son compatibles, 0 puede donar a; ab.")

elif (grupos == "0 y b") or (grupos == "b y 0"):
    print("Los grupos introducidos son compatibles, 0 puede donar a; b.")
    
else: 
    print("Los grupos introducidos, no son correctos, inténtalo de nuevo.")
"""

    


