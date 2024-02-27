import sys


def m_splitA(matr):
    matr = matr.split(',')
    matr = [c.split(' ') for c in matr]
    matr = [[float(c) for c in r if c != ' '] for r in matr]

    return matr

def m_splitB(lst):
    lst = lst.split(',')
    lst = [float(c) for c in lst]
  
    return lst


def gauss(A, B):
    i = 0 
    for x in A:
        x.append(B[i]) 
        i += 1 
    n = len(A)
    X = [0]*n
    for i in range(n):
        if A[i][i] == 0:
                return 'Error: no solution'
        for j in range(i + 1, n):
            d = A[j][i]/A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - d*A[i][k]
 

    x[n - 2] = A[n - 2][n - 1]/A[n - 1][n - 1]
    for i in range(n - 2, - 1, -1):
        x[i] = A[i][n-1]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j]*x[j]
        x[i] = x[i]/A[i][i]    
    return x


if len(sys.argv) != 3:
    print('Error: invalid input')
else:
    A = m_splitA(sys.argv[1])
    B = m_splitB(sys.argv[2])
    if  len(A) > len(A[0]):
        print('Error: no solution')
    elif len(A) != len(B):    
        print('Error: incompatible sizes of matrices')
    else:
        X = gauss(A, B)    
        print(X)

    


#python3 gaussmethod.py "1 -1 1,2 1 -2,1 2 3" "-2,6,2"   
#python3 gaussmethod.py "4 2,1 -3" "2,4" 
#python3 gaussmethod.py "2 -3 -4 5,4 -6 1 -1,6 -9 1 2,2 -3 -2 -4" "-13,14,13,9" 
#python3 gaussmethod.py "1 1 2,3 4 5,1 3 4,5 3 1,4 2 0" "1,2,3,4,5"
#python3 gaussmethod.py "1 -1 -4 -5,2 3 -1 2,2 6 1 -2,4 5 2 -1" "-2,-3,1,4"
#python3 gaussmethod.py "4 2,1 -3"  "1"
#python3 gaussmethod.py "1 2 -3 5,1 3 -13 22,3 5 1 -2,2 3 4 -7" "1,-1,5,4" #бесконечное множество решений == нет решений
#python3 gaussmethod.py "1 -2 3 -4,3 3 -5 1,-2 1 2 -3,3 0 3 -10" "2,-3,5,8" #нет решений