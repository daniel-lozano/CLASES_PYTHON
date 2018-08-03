import numpy as np
import matplotlib.pyplot as plt

def y_sol(x):
    return np.cos(3*x)#np.e**(-x)

def f(x,y):
    return -3*np.sin(3*x)#-np.e**(-x)
x=np.linspace(0,4*np.pi)
dx=x[1]-x[0]
y0=y_sol(x[0])



#dy/dx=-y
#newton integral---------------------------------------------
y_1=np.zeros(len(x))
y_1[0]=y0

for i in range(1,len(x)):
    y_1[i]=y_1[i-1]+dx*f(x[i-1],y_1[i-1])

#Runge-kutta----------------------------------------------------
y_2=np.zeros(len(x))
y_2[0]=y0
for i in range(len(x)-1):
    
    k1=dx*f(x[i],y_2[i])
    k2=dx*f(x[i]+0.5*dx,y_2[i]+0.5*k1)
    k3=dx*f(x[i]+0.5*dx,y_2[i]+0.5*k2)
    k4=dx*f(x[i]+dx,y_2[i]+k3)
    y_2[i+1]=y_2[i]+(1.0/6)*(k1+2*k2+2*k3+k4)

#plt.plot(x,y_sol(x),label="exact")

plt.semilogy(x,abs((y_sol(x)-y_1)),label="newton")
plt.semilogy(x,abs(y_sol(x)-y_2),label="Runge")

plt.legend()
plt.show()


