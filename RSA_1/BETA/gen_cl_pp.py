# -*- coding: utf-8 -*-
from RSA_1.RSA import mcd, inverso
from RSA_1.GEN import t_mr
import random
#En este modulo se genera la clave publica y privada

def Keypp():
    t_mr.generar()
    p=t_mr.salida[0]
    q=t_mr.salida[1]
    n=(p)*(q)# producir n
    phin=(p-1)*(q-1)#producir phi(n)
    #obtener e
    e=2
    while mcd.mcd(e,phin)!= 1:
        e=random.randint(1,phin)
    d=inverso.inverso(e,phin)
    
    return [e, d, n, p, q, phin]

#almacenar los componentes y las claves generadas
#clave.key(clave privada) clave.cr(clave publica)
#los numeros generadores se almacenaran en un archivo
#componentes.gcl(numeros [pq,phin] y nuevamente las claves kpp)
def savekey(comp):
    """crea 2 archivos almacenados en el directorio actual,
    que contienen la clave publica y privada generada"""
    with open('clave.key', mode='w') as key:
        key.write(str(comp[0])+'\n'+str(comp[2]))

    with open('clave.cr', mode='w') as pub:
        pub.write(str(comp[1])+'\n'+str(comp[2]))


def savecomp(comp):
    """crea 1 archivo almacenado en el directorio actual
    que contiene los valores que generan la clave publica
    y privada(con fines informativos, se desaconseja almacenarlos)"""
    with open('componentes.gcl', mode='w') as key:
        key.write(str(comp[3])+'\n'+str(comp[4])+'\n'+str(comp[5]))

def Generar_Claves():
    """aplica lor procedimientos anteriores para generar las claves """
    salida=Keypp()
    savekey(salida)
    savecomp(salida)
