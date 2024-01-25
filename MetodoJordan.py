import math

def jordan(a, b):

    n = len(a)

    for k in range(0, n):
        for j in range(k+1, n):
            a[k][j] = a[k][j] / a[k][k]

        b[k] = b[k] / a[k][k]
        a[k][k] = 1

        print("Matriz: \n%s" % matriz(a))
        print(b)
        print('\n')

        for i in range(0, n):
            if i != k:
                m = - a[i][k] / a[k][k]

                for j in range(k+1, n):
                    a [i][j] = (m * a[k][j]) + a[i][j]

                b[i] = (m * b[k]) + b[i] 
                a[i][k] = 0
            
        print("Matriz: \n%s" % matriz(a))
        print(b)
        print('\n')

    return b

def identidade(n):

    m = []
    for i in range(0, n):
        linha = [0] * n
        linha[i] = 1
        m.append(linha)

    return m

def matriz(M):

    m = len(M)
    n = len(M[0])
    s = ""

    for i in range(m):
        for j in range(n):
            s+= "%9.3f " % M[i][j]
        s+= "\n"

    return s

a = [[87, 30, 93, 110],
     [245, -88, 115, -451],
     [523, -840, -235, 114],
     [210, -810, -132, 215]
     ]

b = [164, -497, -808, -1063]

i = identidade(3)  
print("Ordem 3: \n%s" % matriz(i))
x = jordan(a, b)
print('\n')
print('Resultado: ')
print(x)



