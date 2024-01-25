import math
import numpy as np

#Intervalos
a = 2
b = 3
e = 1 * (10**-6) #Precisão

def f(x):   #Calcular a raiz
    return  (3 * math.cos(math.radians(x))) - (np.exp(x/2)) #Equação

cont = 0
xi = (a*f(b) - b*f(a))/(f(b)-f(a))

if f(a)*f(b) < 0:
    while(math.fabs(f(xi)) > e):  #f(xi) em módulo
        cont += 1
        xi = (a*f(b) - b*f(a))/(f(b)-f(a))
        print('\n')
        print('Iteracao: ', cont)
        print('Valor xi: ', xi)
        print('Valor a: ', a)
        print('Valor b: ', b)
        print('Valor f(xi): ', f(xi))
        if f(xi) == 0:
            print('\n')
            print('Raiz da funcao: ', xi)
            break
        else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
    print('\n')
    print('Iteracao: ', cont)
    print('Valor da raiz e: ', xi)
    print('Valor f(x): ', f(xi))

else: 
    print('\n')
    print('Nao existe raiz neste intervalo!')

