# -*- coding: utf-8 -*-
def expmod(a,n,m):
    """Utiliza la exponenciacion modular
    para obtener la propiedad de congruencia
    ENTRADA:(3 VALORES)
    la base,potencia y el modulo
    SALIDA:(1 VALOR)
    el valor que cumple la congruencia dada.
    """
    exp=1
    x=a%m
    while n>0:
        if (n%2)==1:
	    exp=(exp*x)%m
	x=(x*x)%m
	n=n/2
    return exp
