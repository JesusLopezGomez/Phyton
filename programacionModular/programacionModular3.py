from curses.ascii import islower, isupper
"""
Diseñe una función llamada caracteresEnCadena que tenga una cadena de caracteres y un carácter como
parámetros de entrada y devuelve cuántas veces aparece ese carácter en la cadena. Debería
hacer si la cadena y el carácter son minúsculas o mayúscula

#1
def caracterEnCadena(caracter):
    cadenaCaracteres = "aseadvfgula".lower()
    contador = 0
    for letra in cadenaCaracteres.lower():
        if caracter.lower() == letra.lower():
            contador += 1
    return contador

print(caracterEnCadena("a"))
"""
"""
Diseñe una función llamada lowCaseInString que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son letras minúsculas.

#2
def lowCaseInString(cadenaCaracteres):
    contador = 0
    for i in range(0,len(cadenaCaracteres)):
        if islower(cadenaCaracteres[i]):
            contador += 1
    return contador

print(lowCaseInString("JeSuS"))
"""

"""
Diseñe una función llamada upperCaseInString que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son letras mayúsculas.

#3
def upperCaseInString(cadenaCaracteres):
    contador = 0
    for i in range(0,len(cadenaCaracteres)):
        if isupper(cadenaCaracteres[i]):
            contador += 1
    return contador

print(upperCaseInString("JeSuS"))
"""

"""
Diseñe una función llamada numberInString que tenga una cadena de caracteres como parámetro, el
El método debe devolver cuántos de esos caracteres son números.

#4

def numberInString(cadenaCaracteres):
    contador = 0
    for i in range(0,len(cadenaCaracteres)):
        if cadenaCaracteres[i] in "0123456789" :
            contador += 1
    return contador

print(numberInString("jesus2003"))
"""

"""
Diseñe una función llamada palíndromo que tenga una cadena de caracteres como parámetro y devuelva
verdadero si es un palíndromo o falso en otro caso. Una palabra es un palíndromo, si se lee el
lo mismo de izquierda a derecha que de derecha a izquierda, ignorando los blancos. Por ejemplo: "anilina" o "el
abad le dio arroz al zorro" Para simplificar el problema, se puede suponer que los caracteres simples
se utilizan, es decir, sin tildes ni diresis.
#5

def palindromo(cadenaCaracteres):
    reverso = ""
    opcion = True
    for i in cadenaCaracteres:
        reverso = i + reverso
    if reverso == cadenaCaracteres:
        opcion = True
    else:
        opcion = False
    return opcion

print(palindromo("dabalearrozalazorraelabad"))

def palindromo(palabra):
    tmp = palabra[0:len(palabra)//2]
    for i in range(len(palabra)//2, len(palabra)):
        if tmp[i] == palabra[::-1]:
            
print(palindromo("anilina"))
"""
"""
Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.
#6

def buscarPalabra(frase, palabra):
    posicion = 0
    for letra in frase:
        if posicion < len(palabra) and palabra[posicion] == letra:
            posicion += 1
    return posicion == len(palabra)
print(buscarPalabra("paeecadtraoñ", "pedro"))
"""
"""
Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la
tercera.

#7
def sustituir(cadena,palabra,sustituta):
    resultado,tmp = "", ""
    ipalabra = 0
   
    for i in range(len(cadena)):
        
        if cadena[i] == palabra[ipalabra]:
            tmp += palabra[ipalabra]
            ipalabra += 1
            
            if len(palabra) == ipalabra:
                ipalabra = 0
                resultado += sustituta
                tmp = ""
                #sustituir
        
        else:
            resultado += tmp + cadena[i]
            ipalabra = 0
            
    return resultado

print(sustituir("te vendo la moto", "vendo", "compro"))
"""

"""
Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
#8
def vocalesEnPalabra(palabra):
    palabra = palabra.lower()
    contador = 0
    acomVocal = ""
    tmp = ""
    for i in range(0,len(palabra)):
        if palabra[i] in "aeiou":
            acomVocal += palabra[i]
            contador += 1
    for i in range (0,len(acomVocal)):
        if acomVocal[i] == tmp:
            contador -= 1
        tmp = acomVocal[i]
    return contador

print(vocalesEnPalabra("jesuus"))
"""

"""
Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio"

#9

def deformarCadena(cadena):
    cadena = cadena.lower()
    consonantes = ""
    vocales = ""
    union = ""
    for i in range (0,len(cadena)):
        if cadena[i] in "bcdfghjklmnñpqrstvxzwy":
            consonantes += cadena[i]
        if cadena[i] in "aeiou":
            vocales += cadena[i]
        union = consonantes + vocales
    return union

print(deformarCadena("tevendieronlamoto"))
"""
"""
Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3

#10

def palabrasEnLaCadena(cadena):
    contador = 0
    if cadena[0] != " ":
        contador += 1
    for i in range(len(cadena)-1):
        if cadena[i] == " " and cadena[i+1] != " ":
            contador += 1
    return contador

print(palabrasEnLaCadena(" jesus lopez "))
"""           
