def dameNumero():
    from random import randint
    numero1,numero2= 2,12
    numeroAleatorio1 = randint(numero1, numero2)
    numeroAleatorio2 = randint(numero1, numero2)
    return numeroAleatorio1 + numeroAleatorio2

MENU="""
-----------------------
1.    Apostar
2.    Añadir más saldo
3.    Mostrar saldo
4.    Retirarse
-----------------------
"""

opcion = 2
banco = 0
while opcion != 4:
    if opcion == 1:
        numeroApostado = int(input("Introduzca el número que deseea apostar: "))
        dineroApostado = float(input("Introduzca la cantidad que deseea apostar: "))
        if dineroApostado > 0:
            if dineroApostado <= banco:
                if numeroApostado == dameNumero():
                    banco += dineroApostado*2
                    print(f"Has ganado el numero aleatorio es: {dameNumero()}")
                elif dameNumero() > numeroApostado:
                    banco -= dineroApostado/2
                    print(f"Has perdido la mitad... El numero aleatorio es: {dameNumero()}")
                else:
                    banco -= dineroApostado
                    print(f"Has perdido... El numero aleatorio es: {dameNumero()}")
            else:
                print(f"No puedes apostar más del dinero que tienes en tu tarjeta: {banco}€")
        else:
            print("Vuelve a intentarlo apostando una cantidad mayor que 0.")
    elif opcion == 2:
        saldoAñadido = float(input("Introduce la cantidad de saldo deseeada para empezar a apostar: "))
        if saldoAñadido > 0:
            banco += saldoAñadido
        else:
            print("Vuelve a intentarlo añadiendo una cantidad de saldo mayor que 0.")
    else:
        print(f"{banco}€")
    
    print(MENU)
    opcion = int(input("Introduce una de las opciones: "))
    
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        opcion = int(input("Introduce una opcion correcta(1,2,3,4): "))
        
print("Salido de JacaBet...")
