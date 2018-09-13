import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import *
from scipy.linalg import expm

a=np.array([[0.,1.],[0.,0.]])
ad=np.transpose(a)
n=np.matmul(ad,a)
I=np.eye(2)

J=1
U=-2

print("a=")
print(a)
print("ad=")
print(ad)
print("n=")
print(n)
print("I=")
print(I)

H=J*(np.kron(ad,a)+np.kron(a,ad))+U*(np.kron(I,n)+np.kron(n,I))
Num=np.kron(I,n)+np.kron(n,I)
print("Hamiltoniano")
print(H)

T=1.
N=10000
t=T/N

A=matrix_power(expm(-1j*t*H),N)

print("Final state")
x=np.array([0,1,1,0])/np.sqrt(2)
print(x)

print("initial state")
sol=solve(A,x)#A*b=x
print(sol)

print("average particle number")
ni=np.matmul(np.matrix.conjugate(sol),np.matmul(Num,sol))

nf=np.matmul(np.matrix.conjugate(x),np.matmul(Num,x))
print(abs(ni))
print(nf)

