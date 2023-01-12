"""
20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
"""

meses = 20

precioinicio = 10

total = 0

print(f"Mes 1 = {precioinicio}€")
for i in range (2, 21):
    precioinicio = precioinicio*2
    total += precioinicio
    print(f"Mes {i} = {precioinicio}€")
    
print(f"El total es de {total+10}€")
    
    

