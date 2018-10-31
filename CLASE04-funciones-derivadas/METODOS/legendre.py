import numpy as np
import matplotlib.pyplot as plt
import sys
from sympy import *


def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def poly(x,n,fact):
    return ((x**2-1)**n)/(fact(n)*2**n)

def deriva(F,x,dx):
#    Fp=(1./dx)*(F[1:]-F[0:-1])
#    xp=x[0:-1]
#    
    Ft_p=[]
    xp=x[1:-1]
    for i in range(1,len(x)-1):
        Ft_p.append((0.5/dx)*(F[i+1]-F[i-1]))

    return Ft_p,xp


N=100000
x=np.linspace(-1,1,N)
dx=x[1]-x[0]
polynomia1=poly(x,1,factorial)
polynomia2=poly(x,2,factorial)


P0=poly(x,0,factorial)
P1=(1.0/dx)*(polynomia1[1:]-polynomia1[0:-1])
x1=x[0:-1]

P2=[]
x2=x[1:-1]
for i in range(1,len(polynomia2)-1):

    P2.append((polynomia2[i+1]-2*polynomia2[i]+polynomia2[i-1])/dx**2)

plt.title("$ \mathrm{Legendre\ Polynomials}$")
plt.xlabel("$ x $")
plt.plot(x,P0,label=" $ P_0 $")
plt.plot(x1,P1,label=" $ P_1 $")
plt.plot(x2,P2,label=" $ P_1 $")
plt.grid()
plt.legend()
plt.show()

N=input("Degree of Legendre polinomia to calculate: ")

for i in range(0,N):
    Fd=poly(x,i,factorial)
    xd=x
    for j in range(i):
        Fp,xp=deriva(Fd,xd,dx)
        Fd=Fp
        xd=xp
    if(i==0):
        xp=xd
        Fp=Fd
    
    plt.plot(xp,Fp,"--",label="$ P_"+str(i)+" $")


plt.legend()
plt.grid()
plt.show()

x=Symbol("x")
for n in range(0,N):
    print("P_"+str(n)+"=", Mul(1./(factorial(n)*2**n),diff((x**2-1)**n,x,n))    )








