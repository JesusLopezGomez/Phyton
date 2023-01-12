def crear_digito_control(cadenaNumeroSeguridadSocial):
    longitudValida = False
    numeros = "0123456789"
    todosSonNumeros = True
    mensaje = ""
    if len(cadenaNumeroSeguridadSocial) >= 9 and len(cadenaNumeroSeguridadSocial) <= 12:
        longitudValida = True
    for i in range(len(cadenaNumeroSeguridadSocial)):
        if cadenaNumeroSeguridadSocial[i] not in numeros:
            todosSonNumeros = False
        
    resultado = int(cadenaNumeroSeguridadSocial[0:len(cadenaNumeroSeguridadSocial)-2]) % 97
    if todosSonNumeros and longitudValida:
        mensaje = f"Tu digito de control es: {resultado}"
    else: 
        mensaje = f"El numero introducido no es correcto."
    return mensaje
#print(crear_digito_control("110130116424"))

def es_emitido_andalucia(cadenaNumeroTarjetaAndalucia):
    longitudValida = False
    numeros = "0123456789"
    todosSonNumeros = True
    resultado = False
    if len(cadenaNumeroTarjetaAndalucia) >= 9 and len(cadenaNumeroTarjetaAndalucia) <= 12:
        longitudValida = True
    for i in range(len(cadenaNumeroTarjetaAndalucia)):
        if cadenaNumeroTarjetaAndalucia[i] not in numeros:
            todosSonNumeros = False
    calculo = int(cadenaNumeroTarjetaAndalucia[0:2])
    
    if todosSonNumeros and longitudValida:
        if calculo == 4 or calculo == 11 or calculo == 14 or calculo == 18 or calculo == 21 or calculo == 23 or calculo == 29 or calculo == 41:
            resultado = True
    else:
        resultado = False
        
    return resultado

#print(es_emitido_andalucia("110130116424"))




