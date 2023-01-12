"""
Escribir una expresión lógica que cumpla:
a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero
es superior a 300 euros o negativa.
b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22
años.
c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.
d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.
NOTA: Además siempre debe ser Verdadera en el caso contrario al que se formula.
"""

cantidad = 310

print(not(cantidad < 300 or cantidad < 0))