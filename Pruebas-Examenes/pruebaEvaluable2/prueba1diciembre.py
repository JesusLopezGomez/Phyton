
"""
def dni_valido(cadena_dni):
    return len(cadena_dni) == 8 or len(cadena_dni) == 7
    cadena_dni[len(cadena_dni)-1:len(cadena_dni)]
"""
def calcularLetraDni(cadena_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    valido = False
    suma = 0
    numeros_dni = cadena_dni[0:(len(cadena_dni) -1)]
    resultado = int(numeros_dni) % 23
    if (len(cadena_dni) == 9 or len(cadena_dni) == 8):
        if cadena_dni[len(cadena_dni)-1:len(cadena_dni)] in "TRWAGMYFPDXBNJZSQVHLCKE":
            valido = True
            if letras[resultado] == cadena_dni[len(cadena_dni)-1:len(cadena_dni)]:
                valido = True
    else: 
        
        valido = False

    return valido
print(calcularLetraDni("24483609V"))