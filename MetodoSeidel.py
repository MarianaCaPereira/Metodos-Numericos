import math

def norma(v, x):

    n = len(v)
    maxNum = 0
    maxDen = 0

    for i in range(0, n):
        num = abs(v[i]-x[i])
        if num > maxNum:
            maxNum = num
        
        den = abs(v[i])
        if den > maxDen:
            maxDen = den

    return maxNum / maxDen

def matriz(M):

    m = len(M)
    n = len(M[0])
    s = ""

    for i in range(m):
        for j in range(n):
            s+= "%9.3f " % M[i][j]
        s+= "\n"

    return s

def seidel(a, b, eps, iterMax = 50):

    n = len(a)
    x = n * [0]
    v = n * [0]

    for i in range(0, n):
        for j in range(0, n):
            if i != j :
                a[i][j] = (a[i][j]) / a[i][i]

        b[i] = b[i] / a[i][i]

    print("Matriz: \n%s" % matriz(a))
    print(b)

    cont = 1
    for k in range(1, iterMax+1):
        print('\n')
        print("Iteracao: %s" % cont)
        cont = cont + 1

        for i in range(0, n):
            s = 0
            for j in range(0, n):
                if i != j:
                    s = s + (a[i][j] * x[j])
            x[i] = b[i] - s
        
        d = norma(x, v)
        print("D: %s" % d)
        print(v)
        if d <= eps:
            return x
        v = x[:]

a = [[10, 1, 1],
     [2, 10, 1],
     [2, 2, 10],
    ]
b = [14, 12, 13]

eps = 0.0000001
x = seidel(a, b, eps)
print('\n')
print('Resultado: ')
print(x)