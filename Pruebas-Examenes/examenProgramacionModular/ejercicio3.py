def get_posicion_eq_valor(lista):
    resultado = []
    for i in range(len(lista)):
        if lista[i] == i:
            resultado.append(i)
    return resultado

def obtener_frecuencia(lista):
    cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9 = 0,0,0,0,0,0,0,0,0
    for i in range(len(lista)):
        if lista[i] == 1:
            cont1 += 1
        elif lista[i] == 2:
            cont2 += 1
        elif lista[i] == 3:
            cont3 += 1
        elif lista[i] == 4:
            cont4 += 1
        elif lista[i] == 5:
            cont5 += 1
        elif lista[i] == 6:
            cont6 += 1
        elif lista[i] == 7:
            cont7 += 1
        elif lista[i] == 8:
            cont8 += 1
        else:
            cont9 += 1

    return cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9
#print(obtener_frecuencia([1,1,3,4,5,4,6,6,6,4,3,3]))

def obtener_frecuencia1(lista):
    listaFrecuencia=[]
    for i in range(len(lista)):
        listaFrecuencia.append(0)
        
    contadorFrecuencia = 1
    contadorLista = 0
    while contadorFrecuencia < len(lista):
            if lista[contadorLista ] == contadorFrecuencia:
                listaFrecuencia[contadorFrecuencia] += 1
                contadorLista += 1
            else:
                contadorFrecuencia += 1
    return(listaFrecuencia)
        
    
def dameNumero():
    from random import randint
    return randint(0,20)
lista1 = []
for i in range(10):
    lista1.append(dameNumero())
print(lista1)
    
for i in range(30):
    lista1.append(dameNumero())
print(lista1)

"""
[19, 17, 2, 10, 14, 11, 0, 15, 9, 18]
[19, 17, 2, 10, 14, 11, 0, 15, 9, 18, 2, 14, 14, 18, 11, 18, 1, 6, 15, 3, 16, 19, 6, 4, 6, 0, 17, 14, 1, 15, 4, 1, 12, 8, 3, 15, 16, 1, 0, 16]
"""