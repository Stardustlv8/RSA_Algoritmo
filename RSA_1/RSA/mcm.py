# -*- coding: utf-8 -*-
def euclides(a,b):
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

def mcm(a,b):
    """Obtiene el MCM
    ENTRADA:(2 VALORES)
    se ingresan los numeros a analizar
    SALIDA:(1 VALOR)
    se devuelve el maximo comun multiplo de la entrada
    """
    return (a*b)/euclides(a,b)
