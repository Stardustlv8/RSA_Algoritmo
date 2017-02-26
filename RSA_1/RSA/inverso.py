# -*- coding: utf-8 -*-
import euext

def inverso(z,m):
    """retorna el inverso modular
    utilizando el algoritmo euclides
    extendido"""
    r=euext.euext(z,m)
    if r[0] > 0:
        return r[0] % m
    else:
        return (m+r[0])%m
