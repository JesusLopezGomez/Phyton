print("Bienvenido al juego pares o none")

jugador1 = input("¿Pares o nones?: ").lower()
jugador2 = input("¿Pares o nones?: ").lower()


while jugador1 !="pares" and jugador1 != "nones":
    jugador1 = input("Por favor jugador1, introduzca correctamente su elección: ")
    
while jugador2 !="pares" and jugador2 != "nones":
    jugador2 = input("Por favor jugador2, introduzca correctamente su elección: ")

seleccion1 = int(input(f"Has elegido {jugador1}, introduce la cantidad de dedos: "))
seleccion2 = int(input(f"Has elegido {jugador2}, introduce la cantidad de dedos: "))

while (seleccion1 > 5) or (seleccion1 < 0):
    seleccion1 = int(input("Por favor jugador1, ingrese la cantidad correctamente(0-5): "))
    
while (seleccion2 > 5) or (seleccion2 < 0):
    seleccion2 = int(input("Por favor jugador2, ingrese la cantidad correctamente(0-5): "))

totalGanador1 = 0
totalGanador2 = 0
while seleccion1 != 0 and seleccion1 != 0:    
    
    resultado = seleccion1 + seleccion2
    
    if resultado%2 == 0:
        if jugador1 == "pares":
            print("Ganó la partida pares, jugador1.")
            totalGanador1 += 1
        else: 
            print("Ganó la partida pares, jugador2.")
            totalGanador2 += 1
    else: 
        if jugador1 == "nones":
            print("Ganó la partida nones, jugador1.")
            totalGanador1 += 1
            
        else: 
            print("Ganó la partida nones, jugador2")
            totalGanador2 += 1
    
    jugador1 = input("¿Pares o nones?: ").lower()
    jugador2 = input("¿Pares o nones?: ").lower()


    while jugador1 !="pares" and jugador1 != "nones":
        jugador1 = input("Por favor jugador1, introduzca correctamente su elección: ")
        
    while jugador2 !="pares" and jugador2 != "nones":
        jugador2 = input("Por favor jugador2, introduzca correctamente su elección: ")
    
    
    seleccion1 = int(input(f"Has elegido {jugador1}, introduce la cantidad de dedos: "))
    seleccion2 = int(input(f"Has elegido {jugador2}, introduce la cantidad de dedos: "))
    
    while (seleccion1 > 5) or (seleccion1 < 0):
        seleccion1 = int(input("Por favor jugador1, ingrese la cantidad correctamente(0-5): "))
        
    while (seleccion2 > 5) or (seleccion2 < 0):
        seleccion2 = int(input("Por favor jugador2, ingrese la cantidad correctamente(0-5): "))   
print(f"Se acabó el juego, jugador1 ha ganado {totalGanador1} partidas, y jugador2 ha ganado {totalGanador2} partidas. ")
