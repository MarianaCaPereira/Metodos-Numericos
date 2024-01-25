import math

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

def substituicao_sus(a, b):

    n = len(a)
    x = n * [0]

    for i in range(0, n):
        s = 0
        for j in range(0, i):
            s = s + (a[i][j] * x[j])
        
        x[i] = (b[i]-s) / a[i][i]

        print(x)
        print('\n')

    return x

def substituicao_ret(a, b):

    n = len(a)
    x = n * [0]

    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s = s + (a[i][j] * x[j])
        
        x[i] = (b[i]-s) / a[i][i]
        
        print(x)
        print('\n')

    return x

def lu(a):

    n = len(a)
    l = identidade(n)

    for k in range(0, n-1):
        for i in range(k+1, n):

            m = -a[i][k] / a[k][k]
            l[i][k] = -m

            for j in range(k+1, n):
                a[i][j] = m * a[k][j] + a[i][j]
            
            a[i][k] = 0

        print("\n%s" % matriz(a))

    return (l, a)

def lux(l, u, b):

    print('\n')
    print("Ly:b")
    y = substituicao_sus(l, b)

    print('\n')
    print("Ux=y")
    x = substituicao_ret(u, y)

    return x
    

a = [[5, 2, 1],
     [3, 6, -2],
     [2, -4, 10]]

b = [8, 7, 8]

(l, u) = lu(a)
print("L: \n%s" % matriz(l))
print("U: \n%s" % matriz(u))
print('\n')
x = lux(l, u, b) 
print('\n')
print('Resultado: ')
print(x)





 