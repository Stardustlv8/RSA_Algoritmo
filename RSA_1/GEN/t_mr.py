# -*- coding: utf-8 -*-
import random
from emod import expmod

"""n= cantidad de iteraciones a comprobar
   s= valor potencia
   p= numero a comprobar"""
salida=[]

def is_prim(u,s,p):
    """Test de primalidad de mailling-rabin """
    num = random.randint(2,p-2)
    a=long(expmod(num,s,p))
    if a!= 1 and a!=(p-1):
        j=1
	while j<u:
	    a=long(expmod(a,2,p))
	    if a==(p-1):
		return True
	    if a == 1:
		return False
	    j+=1
	return False
    else:
	return True


def primo(p=0):
    """se genera el numero aleatorio y se analiza
    un total de 100 veces para demostrar la base PTF"""
    try:
	if p==2 or p==3 or p==5:
	    return True
        if p<=0:
            p=random.randint(pow(10,149),pow(10,150))

        if p%2==0:
            p+=1
        s=(p-1)
        u=0L
        while s%2==0:
	    u+=1
	    s=s/2
        for i in range(100):
            if is_prim(u,s,p)==True:
                salida.append(p)
	        return True
    except TypeError:
        return False

    return False

def generar():
    """realiza 2 iteraciones para 2 primos grandes"""
    for i in range(2):
        while not primo():
            pass

def genera_1():
    while not primo():
	pass
