'''
Created on Nov 24, 2022

@author: Jesús López Gómez
'''
"""
11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno.
"""
lista1 = [1,"pepe",4,7]
lista2 = [2,"raul",4,8]
def intersect(lista1,lista2):
    union = lista1 + lista2
    for i in range(0,len(lista1)):
        if lista2[i] == lista1[i]:
            union.remove(union[i])
    return union

print(intersect(lista1,lista2))

#Lo único que me ha dado tiempo a hacer es esto que es si la lista son del mismo tamaño, si te la muestras las union de las dos sin repetir ninguno.
         
    
    