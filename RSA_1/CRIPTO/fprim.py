import math


def primo(n,k=2):
    """Realiza la factorizacion en numeros primos
    ENTRADA:(1 VALOR)
    el valor que se va a factorizar
    SALIDA:(UNA LISTA)
    devulve los valores que cumplen la factorizacion.
    """
    resultados=[]
    if n%2==0:
        while n%k!=n:
 	    if n%k==0:
                resultados.append(k)
	        n/=k
            else:
                k+=1
    else:
	raiz=int(math.sqrt(n))
	if raiz*raiz==n:
            resultados.append(raiz)        
            resultados.append(raiz)
	else:
     	    while(1):
	        d=delta(raiz,n)
		if d>0:
		    entero=int(math.sqrt(d))
		    if entero*entero==d:
		        x=raiz
		        y=entero
			if(x-y>1):
		            resultados.append(x-y)		         
		        resultados.append(x+y)
		        break
		raiz+=1		         
    return resultados


def delta(k,n):
    return (k*k)-n


