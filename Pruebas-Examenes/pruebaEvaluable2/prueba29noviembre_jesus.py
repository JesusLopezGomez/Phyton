'''
Created on Nov 29, 2022

@author: jesus lopez gomez
'''

def generar_usuario(nombre, apellido1, apellido2, dni):
    nombre = nombre[0:3]
    apellido1 = apellido1[len(apellido1)-3:len(apellido1)]
    apellido2 = apellido2[0:3]
    dni = dni[len(dni)-5:len(dni)-1]
    usuario = ""
    usuario = nombre + apellido1 + apellido2 + dni  
    return usuario.lower()
MENU='''
------------------
1.Añadir usuario

2.Eliminar usuario

3.Crear usuario

4.Consultar usuarios

5.Borrar usuarios

6.Salir
-------------------
'''

print(MENU)
opcion = 0
lista = ["pepe" , "jesus" , "lopez" , "gomez" , "loco"]
contador = 0
while opcion != 6:
    opcion = int(input("Introduce una de las opciones: "))
    if opcion == 1:
        if len(lista) < 5:
            usuario_valido = input("Introduzca un usuario: ")
            lista.append(usuario_valido)
        else:
            usuario_valido = input("Introduzca un usuario: ")
            lista[contador] = usuario_valido
            contador += 1
            if contador == 5:
                contador = 0
    elif opcion == 2:
        usuario_eliminar = input("Introduce el nombre del usuario que quiere eliminar: ")
        if usuario_eliminar in lista:
            lista.remove(usuario_eliminar)
        else: 
            print("El usuario que ha facilitado no está en la lista.")
    
    elif opcion == 3:
        lista.append(generar_usuario(nombre=input("Introduce un nombre: "), apellido1=input("Introduce apellido: "), apellido2=input("Introduce segundo apellido: "), dni=input("Introduce tu dni: ")))
    
    elif opcion == 4:
        print(f"Los usuarios que tenemos en la lista son los siguientes: {lista}")
        
    elif opcion == 5:
        lista = []
        print("La lista se ha limpiado correctamente.")
        
print("Fin del programa, gracias.")
        
    