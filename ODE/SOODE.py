import numpy as np
from scipy.integrate import odeint #solve ODE equations
import matplotlib.pyplot as plt


'''
    -------------Solving ODE--------------------
    '''

def model(z,t):
    k=1 #alguna constante de la ecuacion diferencial
    x=z[0]
    y=z[1]
    dxdt=-k*y
    dydt= x # esta es la ecuacion diferencial a solucionar
    return [dxdt,dydt]

y0=0
x0=1
z0=[x0,y0]#esta es una condicion inicial de la ODE

t=np.linspace(0,2*np.pi,50) #espacio de interes de la funcion y(t)

z=odeint(model,z0,t)
x=z[:,0]
y=z[:,1]

plt.plot(t,x,"r-",linewidth=2)
plt.plot(t,y,"b.",linewidth=5)
plt.xlabel(" $  t (s) $ ")
plt.legend(["$ \dot{y} $"," $y$ "])
plt.show()
plt.close()
