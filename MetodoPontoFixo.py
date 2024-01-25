import numpy as np 

def f(x):   #Calcular a raiz
    return (5 * (x**3)) - (3 * (x**2)) - 4  #Equação

def g(x):  #Calcular a g(x)
    return  (((3*(x**2)) + 4) / 5)**1/3  #Equação g(x)

cont = 0
x = 0.5 #Valor estimado
e = (1 * (10**-8)) #Precisão

while np.fabs(f(x)) > e:
    print("Iteracao: %i, x =~ %.6f, f(x) =~ %.6f" % (cont, x, f(x)))
    x = g(x)
    cont = cont + 1

print("Iteracao: %i, x =~ %.8f, f(x) =~ %.8f" % (cont, x, f(x)))