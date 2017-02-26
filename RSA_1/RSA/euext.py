# -*- coding: utf-8 -*-
def euclides_ext(a,b,r):
    """Expresa 2 valores como combinacion lineal de su mcd
    ENTRADA:(3 VALORES)
    Los numeros para obtener el mcd
    SALIDA:(1 VALOR)
    en una lista de 2 elementos retorna los valores
    que cumplen la combinacion lineal.
    """
    k=[0,0]
    if a%b==0:
        r[0]=0
        r[1]=1
        return 1
    
    euclides_ext(b,a%b,k)
    x=k[0]
    y=k[1]
    r[0]=y
    r[1]=x-(y*(a/b))
    return r

def euext(a,b):
    """se encarga de retornar lo valores
    obtenidos por el calculo anterior"""
    w=[0,0]
    euclides_ext(a,b,w)

    return w
