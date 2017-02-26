# -*- coding: utf-8 -*-
from RSA_1.RSA import emod
from RSA_1.CRIPTO import TS

# Extrae la clave publica para encriptar (ok)
def getKP(clave):
    salida=[]
    with open(clave) as pub: # clave.cr
        for linea in pub:
            salida.append(long(linea))
    return salida        

# convierte un caracter a su valor numerico de acuerdo a TS (ok)
def parserCN(archivo,simbolo):
    """ENTRADA
    * archivo a encriptar
    * tabla de simbolos deacuerdo a cada letra
       SALIDA
    * tabla con valores numericos"""
    output=[]
    salida=''
    with open(archivo) as a_file:
        for line in a_file:
            salida+=line
    for i in salida:
        output.append(simbolo[i])

    return output

# encripta el valor numerico dado(ok)
def enC(tabla,clave):
    """	ENTRADA(1 lista):
    * Tabla de simbolos numericos a encriptar
        SALIDA(lista con caracteres)
    * Tabla con valores encriptados"""
    cl1, cl2=getKP(clave)
    aux=[]
    for i in tabla:
        aux.append(emod.expmod(i, cl1, cl2))
    return aux

# segundo factor de encriptacion(ok)

def enC2(tabla,simbolos):
    """el segundo factor de autenticacion convierte la lista de 
    numeros decimales a una lista de simbolos."""
    salida=[]
    for x in tabla:
        z=str(x)
        aux=''
        for y in z:
	    aux+=(simbolos[str(y)])
        salida.append(aux)

    return salida

# escribe en un archivo los valores encriptados(ok)
def parser_EC(tabla_e,archivo):
    """ENTRADA(1 lista)
    * Tabla encriptada
       SALIDA(1 archivo)
    * Escribe en un archivo la tabla"""
    with open(archivo, mode='w') as des:
        for c in tabla_e:
            des.write(str(c)+'\n')


def Encriptar(clave, name_file_in, name_file_out):
    """Efectua el procedimiento de encriptacion"""
    simbolos=parserCN(name_file_in,TS.lista)   # devuelve una lista en la forma [XXXXXXXXXXXXX,XXXXXXXXX,XXXXXX]

    encriptado=enC(simbolos,clave) # devuelve una lista en la forma [XXXXXXXXXXXX,XXXXXXXXXX,XXXXXXXX,XXXXXX]

    encriptado2=enC2(encriptado,TS.lista4)    

    parser_EC(encriptado2,name_file_out)    # escribe en un archivo la lista anterios
