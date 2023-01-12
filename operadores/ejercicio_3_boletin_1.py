"""
3. Escribir una expresión lógica que cumpla:
a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60
euros pero igual o inferior a 420 euros.
b) Debe ser Verdadera si el numero contenido en la variable entera numero es impar.
c) Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son
válidas.
d) Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que
estén comprendidas entre 0:0 y 23:59.
e) Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una
persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).
NOTA: Además siempre debe ser Falsa en el caso contrario al que se formula.
"""
#a

#true
precio = 400
precio = 420
print(60<= precio and precio <=420)

#false
precio = 30
precio = 500
print(60<= precio and precio <=420)

#b
numero = (43)
print(numero % 2 == 1)

#c

#true
saldo = 400
dineroSacar = 200
print(saldo >= dineroSacar > 0 )

#false
saldo = 200
dineroSacar = 400
print(saldo >= dineroSacar > 0 )

#d

#true
hora = 12
minutos = 10 
print(hora >= 0 and hora <=23 and minutos >=0 and minutos <=59)

#false
hora = -1
minutos = 60
print(hora >= 0 and hora <=23 and minutos >= 0 and minutos <=59 )

#e
estadoCivil = "s"
print(not(estadoCivil == "S" or estadoCivil == "V" or estadoCivil == "C" or estadoCivil == "D" ))









