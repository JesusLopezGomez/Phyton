from random import randint
#1.
"""
lista = []
listaSustituye = []


def obtenerMayor(lista):
    mayor = lista[0]
    
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            
    return mayor

def obtenerMenor(lista):
    menor = lista[0]
    
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    
    return menor


def obtenerSumaLista(lista):
    suma = 0
    
    for lista in lista:
        suma += lista
       
    return suma

def obtenerMediaLista(lista):
    
    media = len(lista)
    suma = 0
    
    for lista in lista:
        suma += lista
        
    return suma/media
        
def sustituirValorLista(listaSustituye):
    posicion = int(input("Introduzca la posición que quiere sustituir: "))
    
    while posicion < 0:
        posicion = input("Introduzca la posición que quiere sustituir correctamente: ")
    
    valor = int(input("Introduzca el valor que quiere poner en la posición seleccionada: "))
    
    listaSustituye[posicion] = valor
    
    return listaSustituye
    

for i in range (10):
    lista.append(randint(0, 1000))
print(lista)
print(f"El mayor de la lista es {obtenerMayor(lista)}")
print(f"El menor de la lista es {obtenerMenor(lista)}")
print(f"La suma de todos los números de la lista es: {obtenerSumaLista(lista)}")
print(f"La media de todos los números de la lista es: {obtenerMediaLista(lista)}")


for i in range(10):
    listaSustituye.append(randint(0, 1000))
    
print(f"La lista con el valor introducido sustituido es: {sustituirValorLista(lista)}")
"""

#2
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def desplazarDerechaUnaPosicion(lista):
    aBorrar, aEscribir =  0, lista[0]
    for i in range(len(lista)):
        aBorrar=lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)]=aEscribir
        aEscribir = aBorrar
    
    return lista
    
print(desplazarDerechaUnaPosicion(lista))
"""

#3
"""
meses = ["relleno","enero", "febrero" ,"marzo" , "abril" , "mayo" , "junio" , "julio" , "agosto" , "septiembre" , "octubre" , "noviembre" , "diciembre"]
dias = ["relleno" , 31 , 28 , 31 , 30 , 31 , 30 , 31, 31 , 30 , 31 , 30 , 31 ]
dia, mes, año = 1,0,0

while dia > 0:

    dia = int(input("Introduce un día: "))
    mes = int(input("Introduce un mes: "))
    while mes < 0 or mes > 12:
        mes = int(input("Introduce un mes correcto: ")) 
    
    año = int(input("Introduce un año: "))
    
    if (año%4 == 0) and (año%100 != 0) or (año%400 == 0):
        dias[2] = 29 
        
    while dia > dias[mes]:
        dia = int(input("Introduce un dia correcto: "))

    if dia >= 1:
        print(f"{dia} de {meses[mes]} de {año}")

print("Gracias por su colaboración.")
"""

#4
"""
lista = []

def obtenerMayor(lista):
    mayor = lista[0]
    
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            
    return mayor

def obtenerParLista(lista):
    numerosPares = []
    
    for i in range(1,len(lista)+1):
        if lista[0:int(len(lista))]:
            if i%2 == 0:
                numerosPares.append(i)
    
    return numerosPares
            
        

numero = int(input("Introduce número: "))

while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduce número: "))

    
print(lista) 
print(f"El mayor número de la lista es: {obtenerMayor(lista)}")
print(f"Los numeros pares de la lista son los siguiente: {obtenerParLista(lista)}")
"""

#5
"""
lista = ["Di" , "buen" , "dia" , "a" , "papa"]

def reverse(lista):
    reverso = []
    for l in lista:
        reverso = [l] + reverso 
    return reverso

print(reverse(lista))
"""

#6
"""
lista = [1,3,4,5,6]
def estaOrdenada(lista):
    ordenada = True
    
    for i in range(1,len(lista)):
        if lista[i] < lista[i-1]:
            ordenada = False
            
    return ordenada

print(estaOrdenada(lista))
"""


#7

ficha1 = "[3,4]"
ficha2 = "[0,3]"


def fichaValida(ficha):
    return len(ficha) == 5 and (0 <= int(ficha1[1]) <= 6) and (0 <= int(ficha1[3]) <= 6)
def fichasEncajan(ficha1,ficha2):
    validas = (fichaValida(ficha1) and fichaValida(ficha2))
    encajan = ficha1[1] == ficha2[1] or ficha1[1] == ficha2[3] or ficha1[3] == ficha2[1] or ficha1[3] == ficha2[3]
    return validas and encajan

print(fichasEncajan(ficha1, ficha2))




#8
"""
lista = []
listasum = [1,2,3,4,5,6]

def esPrimo(lista):
    esPrimo = []
    for n in lista:
        contador = 0
        for i in range(2,n):
            if n%i == 0:
                contador += 1
        if contador == 0:
            if n > 0:
                esPrimo.append(n)
    return esPrimo
      
def sumatorioLista(lista):
    suma = 0
    for l in lista:
        suma += l
        
    return suma     

def promedioLista(lista):
    suma = 0
    for l in lista:
        suma += l
        
    promedio = suma // int(len(lista))
    
    return promedio

def numerosFactorial(numeros):
    factorial=[]
    acum=1
    for i in numeros:
        acum = acum + acum*i
        factorial.append(acum)
    return factorial

 

#a

lista.append(int(input("Introduce número: ")))
contador = 0
while lista[contador] >= 0:
    lista.append(int(input("Introduce número: ")))
    contador += 1
    
print(esPrimo(lista))


#b



print(sumatorioLista(listasum))


#c

print(promedioLista(listasum))


print(numerosFactorial(listasum))
"""

#9
"""
def numeroMenorK (lista, k):
    numerosMenorK = []
    for i in range(0,len(lista)):
        if lista[i] < k:
            numerosMenorK.append(lista[i])
    return numerosMenorK

def numeroMayorK (lista,k):
    numerosMenorK = []
    for i in range(0,len(lista)):
        if lista[i] > k:
            numerosMenorK.append(lista[i])
    return numerosMenorK

def multiplosK (lista,k):
    multiploK = []
    for i in range(0,len(lista)):
        for l in range(1,k):
            if lista[i] == k * l:
                multiploK.append(lista[i])
    return multiploK

lista = [1,2,3,4,5,6,7,8,9,10,12,13,14]
k = 7


print(f"Números mayores que K: {numeroMenorK(lista, k)}")
    

print(f"Números mayores que K: {numeroMayorK(lista, k)}")
        

print(f"Multiplos de K: {multiplosK(lista, k)}")
"""

#10



"""
def conversorBinarioDecimal(numero):
    numero_decimal = 0 
    posicion=len(numero)-2

    for i in numero:
        numero=int(i)
        numero_decimal+=numero*2**posicion
        posicion -= 1
    
        return numero_decimal

def conversorDecimalBinario(numero):
    numeroBinario = 0
    posicionBinario = 1
    numero=int(numero)
    while numero != 0:
        numeroBinario = numeroBinario+numero%2*posicionBinario
        numero//=2
        posicionBinario*=10
    
    return numeroBinario

numero = input("Introduce un número decimal o binario(Ejemplos: 10100101b, 123d):")

datoAccp = False
if numero[len(numero)-1:len(numero)] == "b":
    while datoAccp == False:
        tmp = str(numero[:-1])
        for i in range(len(tmp)):
            if tmp[i] == "0" or tmp[i] == "1":
                datoAccp = True
            else:
                datoAccp = False
                
        if datoAccp == False:       
            print("Error")
            numero = input("Introduce un número binario válido(Ejemplos: 10100101b):")
    print(conversorBinarioDecimal(numero))     

elif numero[len(numero)-1:len(numero)] == "d":
    numero = int(numero[:-1])
    while numero < 0 :
        numero = input("Introduce un número decimal positivo(Ejemplos: 1243):")
 
    print(conversorDecimalBinario(numero))     

else:
    print("Dato incorrecto")

"""

#11

"""
lista1=[1,2,3,"luis",6,7,2,10]
lista2=[10,2,"pepe", "luis"]

def intersect(lista1,lista2):
    comunes=[]
    for k in lista1:
        for u in lista2:
            if u==k:
                comunes.append(k)
    unicosComunes=[]
    for j in comunes:
        if j not in unicosComunes:
            unicosComunes.append(j)
    return unicosComunes

print(intersect(lista1, lista2))
"""

#12
"""
lista = [1,2,3,4,5,6,7,8]
lista1 = [1,4,7,9]

def unionListas(lista,lista1):
    union = lista + lista1
    listadef = []

    for i in union:
        if i not in listadef:
            listadef.append(i)

    return listadef

print(unionListas(lista, lista1))
"""

#13

"""
nombres = ["pepe", "jose", "josemi", "joseba", "jesus", "raul"]
letra = "J".lower()
lista =[]
for n in nombres:
    if letra == n[0:1]:
        lista.append(n)
print(lista)
"""

#14

"""
lista=["pepe" , "jose" , "manuel" , "jesus"]

def obtenerCadenaMayor(cadena):
    caracteres1=0
    cadenaMayor=""
    compara=[]
    repetido=0
    repetido1=0
    for i in cadena:
        caracteres=len(i)
        if caracteres > caracteres1:
            caracteres1=caracteres
            cadenaMayor=i
    for i in cadena:
        if len(cadenaMayor) == len(i):
            compara.append(i)
    for i in compara:
        repetido=0
        for x in range(len(i)):
            for z in range(1,len(i)):
                if i[x]==i[z]:
                    repetido+=1
        if repetido > repetido1:
            repetido1=repetido
            cadena=i
    return cadena

print(obtenerCadenaMayor(lista))
"""
