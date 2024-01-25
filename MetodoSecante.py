import numpy as np
import math

def f(x):   #Calcular a raiz
    return (3 * math.cos(math.radians(x))) - (np.exp(x/2)) #Equação

cont = 0
e = 1 * (10**-6) #Precisão
x = 1
xn = 3
xn1 = 2

while np.fabs(f(x)) > e:
    x = xn - f(xn) / (f(xn)-f(xn1)) * (xn - xn1)
    xn1 = xn
    xn = x
    print("Iteracao: %i, x =~ %.8f, f(x) =~ %.8f" % (cont, x, f(x)))
    cont = cont + 1

