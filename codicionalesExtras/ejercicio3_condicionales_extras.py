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