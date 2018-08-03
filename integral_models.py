import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)
exact_val=np.cos(0)-np.cos(np.pi)

print("Exact value=",exact_val)

#diferencias finitas-------------------------------------
N=100

x=np.linspace(0,np.pi,N)
dx=x[1]-x[0]
suma=0

for i in range(len(x)):
    suma+=dx*(f(x[i]))

print("diferencias finitas=", suma)

#integral por puntos en espacio----------------------------

N_p=2000
Area=1*np.pi
fraccion=0

for i in range(N_p):
    x_p=np.random.rand()*np.pi
    y_p=np.random.rand()
    if(f(x_p)>y_p):
        fraccion+=1.0/N_p
Area_rand=np.pi*fraccion
print("Area con randoms=", Area_rand)

#integral del trapezoide-----------------------------------
N=100

x=np.linspace(0,np.pi,N)
dx=x[1]-x[0]
suma=0

for i in range(1,len(x)):
    suma+=0.5*dx*(f(x[i])+f(x[i-1]))

print("Area trapezoide=", suma)







