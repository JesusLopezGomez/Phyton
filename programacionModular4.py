'''
1. Diseña un programa que permite guardar el nombre de usuario y contraseña de
hasta 10 usuarios diferentes. Si el usuario ya existe en el sistema, puede hacer
login tras incluir un usuario y contraseña válidas hasta un máximo de tres
intentos, momento en el que se bloquea su cuenta.
Si el usuario no existe, puede crear una cuenta siempre que haya espacio
(máximo 10), para lo que se le pedirá usuario y contraseña, así como la
confirmación de ésta última.
El menú de este programa permitirá identificarse y crear cuentas nuevas, así
como mostrar todos los nombres de usuario existentes sin sus contraseñas.
''' 
MENU="""
-----------------------------------
1.    Inicia sesión
2.    Crear nueva cuenta
3.    Mostar nombres de usuarios
4.    Salir
-----------------------------------
"""
print(MENU)
opcion = int(input("Introduce una opción: "))
listaUsuario = ["jesus", "pepe"]
listaContraseña= ["lope", "gome"]
listaIntentosFallidos = [0,0,0,0,0,0,0,0,0,0]
while opcion != 4:
    
    if opcion == 1:
        print("Bienvenido introduce tu usuario y contraseña para iniciar sesión. ")
        
        usuario_existente=input("Introduce tu nombre de usuario: ")
        contraseña_existente=input("Introduce la contraseña de tu usuario:")
        
        #if usuario_existente in listaUsuario and contraseña_existente in listaContraseña:
        for i in range(len(listaUsuario)):
            if listaUsuario[i] == usuario_existente and listaContraseña[i] == contraseña_existente:
                print("Inicio de sesión correcto.")
        
        if usuario_existente in listaUsuario and not contraseña_existente in listaContraseña:
            for i in range(len(listaUsuario)):
                if listaUsuario[i] == usuario_existente:
                    posicionUsuario = i
                    
            while listaIntentosFallidos[posicionUsuario] < 3 and (usuario_existente in listaUsuario) and not (contraseña_existente in listaContraseña):
                listaIntentosFallidos[posicionUsuario] += 1
                print("El usuario existe, pero la contraseña es incorrecta.")
                contraseña_existente=input("Introduce la contraseña de tu usuario:")
            
            if contraseña_existente in listaContraseña:
                print("Inicio de sesión correcto.")
            
            elif listaIntentosFallidos[posicionUsuario] >= 3:
                print("Cuenta bloqueada, inténtalo de nuevo más tarde...")
        
        if not usuario_existente in listaUsuario and not contraseña_existente in listaContraseña:
            print("El usuario introducido no existe.")
            
    elif opcion == 2:
        if len(listaUsuario) < 10 and len(listaContraseña) < 10:
            listaUsuario.append(input("Introduzca un nombre de usuario: "))
            listaContraseña.append(input("Introduzca una contraseña para el usuario:"))
        else:
            print("No se aceptan más usuarios")
    elif opcion == 3:
        print(listaUsuario)
    print(MENU)
    opcion = int(input("Introduce una opción: "))
    


#calculo1 
"""
1. Escribe un programa Python para calcular la suma de dígitos de un número

def sumarDigitosNumeros(num):
    num = str(num)
    suma = 0
    for i in range(len(num)):
        suma += int(num[i])
    return suma

print(sumarDigitosNumeros(12))
"""

#calculo2
"""
2.Escribir un programa Python para calcular el máximo común divisor (GCD) de dos
enteros positivos
"""
def maximoComunDivisor(num1, num2):
    temp = 0
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

def minimoComunMultiplo(num1,num2):
    return (num1*num2)//maximoComunDivisor(num1, num2)

#calculo4
"""
4.Escribir un programa Python que acepte dos enteros (n e i) y calcule el valor
"""
"""
i = 5
n = 1
acum = 1
resultado = ""
calculoSuma = ""
tmp = str(n)
while acum < i+1:
    resultado += str(n*acum)
    acum += 1
    if acum < i+1:
        calculoSuma += tmp*(acum-1) + " + "
    else:
        calculoSuma += tmp*(acum-1) + " = " + resultado
print(resultado)
print(calculoSuma)
"""   

#ejercicio5
"""
i. leer_fracción: La tarea de esta función es leer por teclado el numerador y el
denominador y la devuelve simplificada (Por ejemplo, si recibe 16/6 ⇒ 8/3)


def leer_fraccion(numerador,denominador):
    numeradorSimplificado = 0
    denominadorSimplificado = 0
    resultado = ""
#Aquí podemos simplificar esta funcion aun más quitando las dos variables innecesarias; 
#numeradorSimplificado y denominadorSimplificado pero las he utilizado para que se vean mejor.
    for i in range(1,10):
        if (numerador%i == 0) and (denominador%i == 0):
            numeradorSimplificado = numerador//i
            denominadorSimplificado = denominador//i
        resultado = str(numeradorSimplificado) + "/" + str(denominadorSimplificado)
    return resultado
print(leer_fraccion(16, 6))
"""
"""
ii. escribir_fracción: muestra por pantalla la fracción; si el denominador es 1, se
muestra sólo el numerador.

def escribir_fraccion(numerador, denominador):
    resultado = str(numerador) + "/" + str(denominador)
    if denominador == 1:
        resultado = numerador
        
    return resultado
print(escribir_fraccion(16, 1))
"""
"""
iii. calcular_mcd: Esta función recibe dos números y devuelve su máximo común
divisor.

def calcular_mcd(numerador, denominador):
    resultado = maximoComunDivisor(numerador, denominador)
    return resultado

print(calcular_mcd(12,6))
"""

def calcular_minimo_comun_divisor(numerador, denominador):
    return (numerador*denominador)//maximoComunDivisor(numerador, denominador)

"""
iv. simplificar_fracción: simplifica una fracción. Para ello hay que dividir el
numerador y denominador por su MCD.
"""
def simplificar_fraccion(numerador,denominador):
    mcd = maximoComunDivisor(numerador, denominador)
    resultado = str(numerador//mcd) + "/" + str(denominador//mcd)
    return resultado

"""
v. sumar_fracciones: recibe dos funciones n1/d1 y n2/d2 y calcula su suma. La
suma de dos fracciones es otra fracción cuyo numerador n=n1*d2+d1*n2 y
denominador d=d1*d2, simplificando la fracción resultado.
"""
def sumar_fracciones(numerador1,denominador1,numerador2,denominador2):
    numeradorSuma = (numerador1 * denominador2) + (denominador1 * numerador2)
    denominadorSuma = denominador1 * denominador2
    resultado = simplificar_fraccion(numeradorSuma, denominadorSuma)
    return resultado
#print(sumar_fracciones(6,5,4,5))

"""
vi. restar_fracciones: resta dos fracciones, siendo el numerador de la resta
n=n1*d2-d1*n2 y el denominador d=d1*d2, simplificando el resultado.
"""
def restar_fracciones(numerador1,denominador1,numerador2,denominador2):
    numeradorResta = (numerador1*denominador2)-(denominador1*numerador2)
    denominadorRestar = denominador1*denominador2
    resultado = simplificar_fraccion(numeradorResta, denominadorRestar)
    return resultado

#print(restar_fracciones(6,5,4,5))

"""
vii. multiplicar_fracciones: recibe dos fracciones y calcula su producto, siendo el
numerador del producto n=n1*n2 y el denominador d=d1*d2 (simplificando).
"""

def multiplicar_fracciones(numerador1,denominador1,numerador2,denominador2):
    numeradorMultiplicacion = numerador1 * numerador2
    denominadorMultiplicacion = denominador1 * denominador2
    resultado = simplificar_fraccion(numeradorMultiplicacion, denominadorMultiplicacion)
    return resultado
#print(multiplicar_fracciones(6,5,4,5))


"""
viii. dividir_fracciones: calcula el cociente de dos fracciones, siendo el numerador
n=n1*d2 y denominador d=d1*n2 (simplificando el resultado).
"""

def dividir_fracciones(numerador1,denominador1,numerador2,denominador2):
    numeradorDivision = numerador1 * denominador2
    denominadorDivision = denominador1 * numerador2
    resultado = simplificar_fraccion(numeradorDivision, denominadorDivision)
    return resultado

#print(dividir_fracciones(6,5,4,5))

MENU = """
##################################
a.    Sumar dos fracciones
b.    Restar dos fracciones
c.    Multiplicar dos fracciones
d.    Dividir dos fracciones
e.    Salir
##################################
"""
"""
opcion = input("Introduzca una de las opciones: ").lower()

while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "e":
    opcion = input("Introduce una opción valida(a,b,c,d,e): ")

while opcion != "e":

    if opcion == "a":
        print(sumar_fracciones(int(input("Introduzca numerador1: ")), int(input("Introduzca denominador1: ")), int(input("Introduzca numerador2: ")), int(input("Introduzca denominador2: "))))
        
    elif opcion == "b":
        print(restar_fracciones(int(input("Introduzca numerador1: ")), int(input("Introduzca denominador1: ")), int(input("Introduzca numerador2: ")), int(input("Introduzca denominador2: "))))
    
    elif opcion == "c":
        print(multiplicar_fracciones(int(input("Introduzca numerador1: ")), int(input("Introduzca denominador1: ")), int(input("Introduzca numerador2: ")), int(input("Introduzca denominador2: "))))
    
    else:
        print(dividir_fracciones(int(input("Introduzca numerador1: ")), int(input("Introduzca denominador1: ")), int(input("Introduzca numerador2: ")), int(input("Introduzca denominador2: "))))

    print(MENU)
    
    opcion = input("Introduzca una de las opciones: ").lower()
    
    while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "e":
        opcion = input("Introduce una opción valida(a,b,c,d,e): ")
    
print("Saliendo del sistema...")
"""

"""
Define una función que calcule el área de un círculo dado su radio
"""
def calcularAreaCirculoConRadio(radio):
    return f"El area del circulo con radio {radio} es {3.14159*(radio**2)}"
"""
Defina una función que dado el radio de un círculo devuelva su longitud
"""
def calcularLongitudConRadio(radio):
    return f"La longitud del circulo con radio {radio} es {2*3.14159*radio}"
"""
Función tal que dadas las coordenadas de dos puntos en el plano devuelve su
distancia euclídea. Un punto en el plano tiene dos coordenadas (abscisa y ordenada), 
por lo tanto, la entrada a esta función son cuatro valores reales
"""
def calcularRaizCuadrada(numero):
    return numero **(0.5)
def calcularDistanciaEuclidiana(x1,x2,y1,y2):
    return calcularRaizCuadrada(((x2 - x1)**2) + ((y2 - y1)**2))
#print(calcularDistanciaEuclidiana(3, -5.1, 3.5, -5.2))
"""
Función tal que dadas las coordenadas de un triángulo en el plano, nos devuelve
su perímetro.
"""
"""
 Función que dado un instante (horas, minutos y segundos) devuelva el número
de segundos transcurridos desde el inicio de un día hasta ese instante.
"""

def calcularSegundos(horas,minutos,segundos):
    return horas*60**2 + minutos*60 + segundos
"""
Crea una función que devuelva la diferencia en segundos entre dos instantes de
tiempo del mismo día. Recibirá como parámetros seis valores, hora, minuto y
segundo de cada uno de los instantes.
"""
def calcularSegunndosEnInstantes(horas1,minutos1,segundos1,horas2,minutos2,segundos2):
    #Esta funcion está realizada en formato 12h.
    return (horas1*60**2 + minutos1*60 + segundos1) - (horas2*60**2 + minutos2*60 + segundos2)
"""
Escriba un programa Python para convertir segundos en día, hora, minutos y segundos.
"""
def calcularSegundosEnDiaHoraMinutoSegundo(dias,horas,minutos,segundos):
    #Esta funcion está realizada en formato 12h.
    return (dias*24)*60**2 + (horas*60**2) + (minutos*60) + segundos
"""
Escribe un programa Python para calcular el número de días entre dos fechas.
    resultado = dia1 - dia2
    if resultado < 0:
        resultado = dia2 - dia1
"""
def calcularDiasEnDosFechas(fecha1,fecha2):
    pass
    