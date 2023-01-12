
print("Ejercicio 13")

alumnos = int(input("Introduzca el número de alumnos que van de viaje: "))

if (alumnos >= 100):
    print("Cada alumno pagará por el viaje " + str(int(alumnos * 65)// alumnos) + "€ y cada alumno pagará a la compañía de autobuses " + str(int(4000//alumnos)) + "€" + ". En total deben pagar: " + str(int(4000//alumnos) + (alumnos * 65)// alumnos ) + "€.")
    
elif (50 <= alumnos <= 99):
    print("Cada alumno pagará por el viaje " + str(int(alumnos * 70)// alumnos) + "€ y cada alumno pagará a la compañía de autobuses " + str(int(4000//alumnos)) + "€" + ". En total deben pagar: " + str(int(4000//alumnos) + (alumnos * 70)// alumnos ) + "€.")
    
elif (30 <= alumnos <= 49):
    print("Cada alumno pagará por el viaje " + str(int(alumnos * 95)// alumnos) + "€ y cada alumno pagará a la compañía de autobuses " + str(int(4000//alumnos)) + "€" + ". En total deben pagar: " + str(int(4000//alumnos) + (alumnos * 95)// alumnos ) + "€.")
    
elif (alumnos < 35):
    print("Cada alumno pagará por el viaje " + str(int(alumnos * 95)// alumnos) + "€ y cada alumno pagará a la compañía de autobuses " + str(int(4000//alumnos)) + "€" + ". En total deben pagar: " + str(int(4000//alumnos) + (alumnos * 95)// alumnos ) + "€.")