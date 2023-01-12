num = int(input("Introduzca un número entre 0 y 10: "))

if (num >= 0) and (num < 10):
    print(f"Aquí tienes la tabla del {num} ")

for i in range(11):
    print(f"{num}*{i} = {num*i}")
    
else:
    print("El número introducido no está entre el 0 y el 10")

