def sep(numero,part):
    """Segmenta un tipo long en mas tipos long
    ENTRADA:(2 VALORES)
    se obtiene el valor a segmentar
    y el numero de segmentos a realizar
    SALIDA:(1 LISTA)
    se devuelven todas las secciones obtenidas
    """
    if numero >0 and part > 0:
	lista=[]
    	cadena=str(numero)
    	tam=len(cadena)
    	inc=tam/part
    	ini=0
    	fin=inc
    	for i in range(part):
    	    lista.append(int(cadena[ini:fin]))
	    ini=fin
	    fin=fin+inc
	return lista                
    else:
	return numero
