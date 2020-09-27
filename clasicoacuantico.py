from operacionesmatrices import *
import matplotlib.pyplot as plt
import numpy as np
def canicas(matriz, estado, clicks):
    a = matriz
    for i in range(clicks):
        a = produmatrint(a, matriz)
    b = accionvecmat(a, estado)
    for i in range(len(b)):
        if b[i] == 1:
            b[i] = "True"
        else:
            b[i] = "False"
    return b
def probclasico(matriz, vector, clicks):
    for i in range(clicks):
        vector = accionvecmat(matriz,vector)
    return vector
def multiplerendija(matriz, clicks):
    a = matriz
    for i in range(clicks):
        matriz = produmatr(matriz, a)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = modulo(matriz[i][j])**2
    return matriz
def grafica(vector):
    y = []
    for i in range(len(vector)):
        y += [i]
    y = np.array(y)
    for i in range(len(vector)):
        vector[i] = round(vector[i] * 100, 2)
    x = np.array(vector)
    plt.bar(y, x, align="center")
    plt.title("probabilidad")
    plt.show()
def modulo(numero):
    ans = (numero.real**2 + numero.imag**2)**0.5
    return round(ans, 2)

    
    
