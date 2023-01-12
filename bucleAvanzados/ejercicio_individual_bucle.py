
peso = int(input("¿Cuánto pesas (unidad: kg): "))
edad = int(input("¿Cuántos años tienes (Recuerda solo escribir el número): "))
tipoVida = input("¿Qué tipo de vida llevas? (Sedentaria/Activa/Muy activa): ").lower()

if(peso < 0):
    print("Se acabó, introduciste un peso incorrecto.")
 
else:
    while (edad <= 0):
        edad = int(input("Error, introduzca su edad de nuevo: "))
        
    while (tipoVida !="sedentaria") and (tipoVida != "activa") and (tipoVida != "muy activa"):
        tipoVida = input("Error, introduzca tipo de vida de nuevo (Sedentaria/Activa/Muy activa): ").lower()
        
    if (edad > 70) and (tipoVida == "sedentaria"):
        print("Lo recomendable sería ir a médico.")
        
    elif (peso > 100):
        print("Lo recomendable sería ir a médico.")
        
    elif (peso > 74.4) and (edad > 50):
        print("Lo recomendable sería ir a médico.")
        
    else: 
        print("No es urgente que acuda al médico si no tiene problemas de salud.")

