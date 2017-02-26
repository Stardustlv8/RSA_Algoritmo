def mcd(a,b):
    """Determina si 2 valores son coprimos entre si.
    ENTRADA:(2 VALORES)
    numeros a analizar
    SALIDA:(TRU/FALSE)
    devuelve un valor boleano con la respuesta.
    """
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
    if a==1:
        return True
    return False
