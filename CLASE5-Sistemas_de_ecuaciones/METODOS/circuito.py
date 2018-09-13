import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import *
from scipy.linalg import expm

R1=1.
R2=2.
R3=3.
R4=4.
R5=5.
V=10.
I=3.667

A=np.array([[0,0,0,R5],[R1+R4,R2,0,0],[0,-R2,R3,0],[1,1,1,1]])

b=[V,V,0,I]


print(A,b)
solution=solve(A,b)
print("Solution=",solution)
print("Ax=",np.matmul(A,solution))

for i in range(len(solution)):
    print("I_"+str(i+1)+"=",solution[i])
I1=1./2
I2=2./2
I3=3./2
I5=5./2

Ap=np.array([[1,0,0,0,-1],[0,1,0,-1,0],[0,0,0,0,I5],[I1,I2,0,I1,0],[0,I2,-I3,0,0]])
bp=[0,0,V,V,0]

print(Ap,bp)
solution=solve(Ap,bp)
print("Solution=",solution)
print("Ax=",np.matmul(Ap,solution))

#print("Final state")
#x=np.array([0,1,1,0])/np.sqrt(2)
#print(x)
#
#print("initial state")
#sol=solve(A,x)#A*b=x
#print(sol)
#
#print("average particle number")
#ni=np.matmul(np.matrix.conjugate(sol),np.matmul(Num,sol))
#
#nf=np.matmul(np.matrix.conjugate(x),np.matmul(Num,x))
#print(abs(ni))
#print(nf)
#
