# -*- coding: utf-8 -*-
def mcd(a,b):
    """Algoritmo de euclides para obtener el MCD
    ENTRADA:(2 VALORES)
    se proporcionan los valores a analizar
    SALIDA: (1 VALOR)
    Se devuelve el maximo comun divisor de la entrada   
    """
    r=1
    if a<b:
        c=a
        a=b
        b=c
    while r > 0:
        c=a/b
        r=a%b
	a=b
        b=r
    return a
