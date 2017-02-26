import re

def analiza_entero(cadena):
    entero = re.compile('(\d+)')
    salida = []
    try:

        s = entero.search(cadena).groups()
        salida = long(s[0])

    except AttributeError:
        return 0L

    return salida


def analiza_enteros(cadena):
    entero = re.compile('(\d+)(\D+)(\d+)')
    salida = []
    try:
        s = entero.search(cadena).groups()
        salida = long(s[0]),long(s[2])
    except AttributeError:
        return (1,1)

    return salida

def analiza_enteros2(cadena):
    entero = re.compile('(\d+)(\D+)(\d+)(\D+)(\d+)')
    salida = []
    try:
        s = entero.search(cadena).groups()
        salida = long(s[0]),long(s[2]),long(s[4])
    except AttributeError:
        return (1,1,1)

    return salida

def ext_val(cadena):
    nombre = re.compile('(\w).txt')
    try:
	s = nombre.search(cadena).groups()
    except AttributeError:
	return False

    if len(s)>0:
        return False
    
    return True

