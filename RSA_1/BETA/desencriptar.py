# -*- coding: utf-8 -*-

from RSA_1.RSA import emod
from RSA_1.CRIPTO import TS

# Extrae la clave publica para encriptar
def getKP(clave):
    salida=[]
    with open(clave) as pub:# clave.key
        for linea in pub:
            salida.append(long(linea))
    return salida

# convierte un caracter a su valor numerico de acuerdo a TS
def parserN(archivo):
    """ENTRADA
    * archivo a encriptar
    * tabla de simbolos deacuerdo a cada letra
       SALIDA
    * tabla con valores encriptados"""
    output=[]
    with open(archivo) as a_file:
        for line in a_file:
            output.append(line.rstrip())	    

    return output

# segundo factor de validacion antes de desencriptar.
def parserN2(tabla,simbolos):
    salida=[]
    for x in tabla:
        aux=''
        for y in x:
            aux+=(simbolos[y])
        salida.append(long(aux))

    return salida

# desencripta el valor numerico dado
def DenC(tabla, clave):
    """ ENTRADA(1 lista):
    * Tabla de caracteres a desencriptar
        SALIDA(lista con caracteres)
    * Tabla con valores desencriptados"""
    cl1, cl2=getKP(clave)
    aux=[]
    for i in tabla:
        aux.append(emod.expmod(i, cl1, cl2))
    return aux

# escribe en un archivo los valores encriptados
def parser_DESEC(tabla_e,simbolos,archivo):
    """ENTRADA(1 lista)
    * Tabla desencriptada
       SALIDA(1 archivo)
    * Escribe en un archivo la tabla"""
    with open(archivo, mode='w') as des:
        for c in tabla_e:
            des.write(simbolos[str(c)])


def Desencriptar(clave, name_file_in, name_file_out):
    """efectua el procedimiento de desencriptacion"""
    simbolos=parserN(name_file_in)

    desencriptado=parserN2(simbolos,TS.lista3)

    desencriptado2=DenC(desencriptado,clave)

    parser_DESEC(desencriptado2,TS.lista2,name_file_out)

