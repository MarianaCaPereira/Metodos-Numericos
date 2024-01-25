import numpy as np
import math

def f(x):   #Calcular a raiz
    return (3 * math.cos(math.radians(x))) - (np.exp(x/2)) #Equação  #Equação

def h(x):  #Calcular a raiz da derivada
    return  (-3 * math.sin(math.radians(x))) -  ((np.exp(x/2) * x/2))#Equação da derivada

cont = 0
x = 0.5  #Valor estimado
e = 1 * (10**-6) #Precisão

while np.fabs(f(x)) > e:
    print("Iteracao: %i, x =~ %.8f, f(x) =~ %.8f" % (cont, x, f(x)))
    x = x - f(x) / h(x)
    cont = cont + 1

print("Iteracao: %i, x =~ %.8f, f(x) =~ %.8f" % (cont, x, f(x)))