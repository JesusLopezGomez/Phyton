#1
"""
Diseñe un método llamado computeFactorial que reciba un entero positivo y
devuelve el factorial para ese número. Si el número es negativo, el método debe
devuelve Ninguno.


def computerFactorial(numero):
    factorial = 1       
    
    if numero >= 0:
        for i in range(1,num):         
            factorial=(factorial+(factorial*i))
    elif numero <= 0:
        factorial = None
    return factorial
             
    
num = int(input("Inserta un número entero positivo: "))  
print (computerFactorial(num))
"""
#2
"""
Diseñe un método llamado esAñoBisiesto que reciba un número y devuelva Falso para
años comunes y True para años bisiestos. Usted puede saber que un año se considera
ser un año bisiesto si es divisible por 4, a menos que también sea divisible por 100. Un año no es un
año bisiesto si es divisible por 100 a menos que también sea divisible por 400.


def añoBisiesto(año):
    return(año%4 == 0) and (año%100 != 0) or (año%400 == 0)


assert añoBisiesto(2012) == True
assert añoBisiesto(2020) == True
assert añoBisiesto(2022) == False

print(añoBisiesto(2012))
"""

#3
"""
Diseñe un método llamado computeDaysInMonth que devuelva el número de días para
el mes y el año que se reciben como argumentos. Puede utilizar el método
año bisiesto anterior. Si los valores no son válidos, el método debería devolver -1.

meses = ["relleno","enero", "febrero" ,"marzo" , "abril" , "mayo" , "junio" , "julio" , "agosto" , "septiembre" , "octubre" , "noviembre" , "diciembre"]
dias = ["relleno" , 31 , 28 , 31 , 30 , 31 , 30 , 31, 31 , 30 , 31 , 30 , 31 ]
def añoBisiesto(año):
    return(año%4 == 0) and (año%100 != 0) or (año%400 == 0)

def diasEnMes(mes,año):
    resultado = 0
    if (1 <= mes <= 12):
        if (mes == 2) and (añoBisiesto(año)):
            dias[mes] = 29
            resultado = dias[mes]
        else:
            resultado = dias[mes]
    else:
        resultado = -1
    return resultado



mes = int(input("Indica el números del mes: "))
año = int(input("Indica el año: "))
print(diasEnMes(mes, año))
"""

#4
"""
Diseñar un método denominado getDayOfWeek que reciba una lista que contenga tres enteros
(día, mes y año) y devuelve el día de la semana para esa fecha (lunes,
Martes, miércoles, jueves, viernes, sábado, domingo).
Puede usar el siguiente algoritmo para obtener un número entre 0 (domingo) y 6
(sábado) correspondiente al día de la semana para una fecha determinada:
a = (14 - mes) / 12
y = año – a
m = mes + 12 * a – 2
d = (día + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
    for i in range(int(d)+1):
        if i == int(d):
            resultado = i

lista=[]


def obtenerDiaSemana(lista):
    semana = ["domingo", "lunes" , "martes" , "miercoles" , "jueves" , "viernes" , "sabado"]
    a = (14 - lista[1]) // 12
    y = lista[2] - a
    m = lista[1] + 12 * a - 2
    d = (lista[0] + y + y//4 - y//100 + y//400 + (31*m)//12) %7
    return semana[int(d)]
    


lista.append(int(input("Introduce un día:")))
lista.append(int(input("Introduce un mes:")))
lista.append(int(input("Introduce un año:")))

print(obtenerDiaSemana(lista))
"""


#5
"""
def powerit (numero1,numero2):
    contador = 1
    for i in range(numero2):
        contador*=numero1
        
    return contador

print(powerit(5, 3))
"""     
        
#6 

#7     
"""
Diseñar un método llamado isPrime que reciba un número entero positivo mayor
que 0 como parámetro. El método debe devolver True si el número es primo o False si
no prime. Si el parámetro no es válido, el método debe devolver None.

def esPrimo(numero):
    contador = 0
    esPrimo = True
    for i in range(2,numero):
        if numero%i == 0:
            contador += 1
            esPrimo = False
    if contador == 0:
        if numero > 0:
            esPrimo = True
        else:
            esPrimo = None
    return esPrimo


print(esPrimo(3))
"""

#8
"""
Diseñar un método denominado solveSecondOrderEquation que reciba tres enteros
Números positivos correspondientes a los coeficientes de una ecuación de segundo orden
(hacha2+bx+c=0) y calcula sus posibles soluciones. Si los parámetros no son válidos, el
método debe devolver Ninguno
"""


#9
"""
Diseñe un método llamado getPrimeDivisors que reciba un número positivo como
y devuelve una lista que contiene sus divisores principales. Si el parámetro no es válido
el método debe devolver None.


def divisoresPrincipales(numero):
    divisores = []
    for i in range (1,numero):
        if numero%i == 0:
            divisores.append(i)
    if numero > 0:
        return divisores
        
print(divisoresPrincipales(8))
"""

#10
"""
Diseñar un método denominado isFriendNumber que reciba dos números positivos y
devuelve True si los números son amigos, False en caso contrario. Dos números son
considerados amigos si la suma de sus divisores, excepto el número dado, es igual
al segundo y viceversa.
"""

def numerosAmigos(numero1,numero2):
    acomulador1 = 0
    acomulador2 = 0
    amigos = True
    for i in range (1,numero1):
        if numero1%i == 0:
            acomulador1 += i
    for i in range (1,numero2):
        if numero2%i == 0:
            acomulador2 += i
    if acomulador1 == acomulador2:
        amigos = True
    else:
        amigos = False
    return amigos

print(numerosAmigos(2,8))

    