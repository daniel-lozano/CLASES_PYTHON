import numpy as np
import matplotlib.pyplot as plt
import sys
from sympy import *



def factor(x,n):
    return pow(-1,n)*np.exp(x**2)

def function(x):
    return np.exp(-x**2)

def deriva(F,x,dx):
#    Fp=(1./dx)*(F[1:]-F[0:-1])
#    xp=x[0:-1]
#    
    Ft_p=[]
    xp=x[1:-1]
    for i in range(1,len(x)-1):
        Ft_p.append((0.5/dx)*(F[i+1]-F[i-1]))

    return Ft_p,xp


N=10000
x=np.linspace(-2,2,N)
dx=x[1]-x[0]
func=function(x)
fac0=factor(x,0)
fac1=factor(x[0:-1],1)
fac2=factor(x[1:-1],2)



H0=fac0*func
H1=fac1*(1.0/dx)*(func[1:]-func[0:-1])
x1=x[0:-1]

H2=[]
x2=x[1:-1]
for i in range(1,len(func)-1):
    H2.append((func[i+1]-2*func[i]+func[i-1])/dx**2)
H2=H2*fac2

plt.title("$ \mathrm{Hermite\ Polynomials}$")
plt.xlabel("$ x $")
plt.plot(x,H0,label=" $ H_0 $")
plt.plot(x1,H1,label=" $ H_1 $")
plt.plot(x2,H2,label=" $ H_2 $")
plt.grid()
plt.legend()
plt.show()


N=input("Degree of Hermite polynomia to calculate: ")

for i in range(0,N):
    Fd=function(x)
    xd=x
    for j in range(i):
        Fp,xp=deriva(Fd,xd,dx)
        Fd=Fp
        xd=xp
    if(i==0):
        xp=xd
        Fp=Fd
    
    plt.plot(xp,factor(xp,i)*Fp,"-",label="$H_"+str(i)+" $")

plt.ylim(-30,30)
plt.legend()
plt.grid()
plt.show()

x=Symbol("x")
for n in range(0,N):
    print("H"+str(n)+"=", Mul(((-1)**n)*exp(x**2),diff(exp(-x**2),x,n))    )






