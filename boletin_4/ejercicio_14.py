
print ("Ejercicio 14")
dia = input("¿Qué día de la semana realizó la llamada?: ")
turno = input("¿Realizó la llamada en turno de tarde o de mañana?(tarde/mañana): ")
minutos = int(input("¿Cuantos minutosutos duró la minutos que acabas de realizar?: "))


if (minutos <= 5) and (dia == "domingo"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(minutos * 1) + (3*minutos)/100} euros.")
    
elif (minutos > 5 and minutos <= 8) and (dia == "domingo"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 +(minutos * 0.80 - 5)) + (3*minutos)/100} euros. ")

elif (minutos > 8 and minutos <=10) and (dia == "domingo"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (3 * 0.80 - 5) + (minutos * 0.70 - 2.4)) + (3*minutos)/100} euros.")
    
elif (minutos > 10) and (dia == "domingo"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (3 * 0.80 - 5 ) + (2 * 0.70 - 2.4) + (minutos * 0.50)) + (3*minutos)/100} euros.")


elif (minutos <=5) and (turno == "tarde"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(minutos * 1) + (10*minutos)/100} euros.")

elif (minutos > 5 and minutos <= 8) and (turno == "tarde"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (minutos * 0.80)) + (10*minutos)/100} euros. ")

elif (minutos > 8 and minutos <=10) and (turno == "tarde"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (3 * 0.80) + (minutos * 0.70)) + (10*minutos)/100} euros.")
    
elif (minutos > 10) and (turno == "tarde"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (3 * 0.80) + (2 * 0.70) + (minutos * 0.50)) + (10*minutos)/100} euros.")


elif (minutos <=5) and (turno == "mañana"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(minutos * 1) + (15*minutos)/100} euros.")

elif (minutos > 5 and minutos <= 8) and (turno == "mañana"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (minutos * 0.80)) + (15*minutos)/100} euros. ")

elif (minutos > 8 and minutos <=10) and (turno == "mañana"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (3 * 0.80) + (minutos * 0.70)) + (15*minutos)/100} euros.")
    
elif (minutos > 10) and (turno == "mañana"):
    print(f"La minutos de duración {minutos}min tiene un coste de: {(5 + (3 * 0.80) + (2 * 0.70) + (minutos * 0.50)) + (15*minutos)/100} euros.")
