import numpy as np

def factorial(n):

    total=1.0
    for i in range(n):
        total*=(i+1)
    return total

A=[[1.0,0,0],[0,1.0,0],[0,0,1.0]]
B=[[1.0,0,0],[1.0,1.0,0],[1.0,0,1.0]]


C=[[1.0,0,0,0],[0,1.0,0,0],[0,0,1.0,0]]


print "Numero de columnas", len(C[0])
print "numero de filas", len(C)
print C

def multiply_matrix(A,B):
    
    MATRIX=np.zeros([len(A),len(B[0])])
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            cij=0
            for k in range(len(A)):
                cij+=A[i][k]*B[k][j]
            C[i][j]=cij
    return MATRIX

def sum_matrix(A,B):
    
    C=np.zeros(np.shape(A))
    
    for i in range(len(A[0])):
        for j in range(len(A[0])):
            C[i][j]=A[i][j]+B[i][j]

    return C

#print multiply_matrix(A,B)
#print sum_matrix(A,B)
print multiply_matrix(A,C)
