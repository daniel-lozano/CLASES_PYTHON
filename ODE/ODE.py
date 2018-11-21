s
import numpy as np
from scipy.integrate import odeint #solve ODE equations
import matplotlib.pyplot as plt


'''
-------------Solving ODE--------------------
'''

def model1(y,t):
    k=0.3 #alguna constante de la ecuacion diferencial
    dydt=-k*y # esta es la ecuacion diferencial a solucionar
    return dydt

y0=5 #esta es una condicion inicial de la ODE

t=np.linspace(0,20,50) #espacio de interes de la funcion y(t)

y=odeint(model1,y0,t)

plt.plot(t,y)
plt.xlabel(" $  t (s) $ ")
plt.ylabel(" $  y (m) $ ")
plt.show()
plt.close()

"""
-------------------Solving with parameters------------------
"""

def model2(y,t,k):
    dydt=-k*y
    return dydt

k1=0.3
y1=odeint(model2,y0,t,args=(k1,))#arg es para dar los argumentos el (k,) es para dar una tupla
k2=0.2
y2=odeint(model2,y0,t,args=(k2,))
plt.plot(t,y1,label=str(k1))
plt.plot(t,y2,label=str(k2))
plt.xlabel(" $  t (s) $ ")
plt.ylabel(" $  y (m) $ ")
plt.title("with arguments")
plt.legend()
plt.show()
plt.close()

"""
-------------------Solving several ODE ------------------
"""

def model3(z,t):
    x=z[0]
    y=z[1]
    dxdt=3.0*np.exp(t/100)
    dydt=3.0-y
    dzdt=[dxdt,dydt]
    return dzdt
x0=0
y0=0
z0=[x0,y0]
t=np.linspace(0,10)

z=odeint(model3,z0,t)#arg es para dar los argumentos el (k,) es para dar una tupla
x=z[:,0]
y=z[:,1]
plt.plot(t,y,label="y(t)")
plt.plot(t,x,label="x(t)")
plt.xlabel(" $  t (s) $ ")
plt.ylabel(" $ Func (m) $ ")
plt.title("several ODE")
plt.legend(["x(t)","y(t)"],loc=2)
plt.show()
plt.close()

"""
-------------------Solving mixed ODE ------------------
"""
t=np.linspace(0,15)
x0=0
y0=0
z0=[x0,y0]

def modelxy(z,t):
    x=z[0]
    y=z[1]
    u=0
    if(t<=5):
        u=0
    else:
        u=2
    dxdt=(-x+u)/2.0
    dydt=(-y+x)/5
    return [dxdt,dydt]


z=odeint(modelxy,z0,t)
x=z[:,0]
y=z[:,1]
plt.plot(t,x)
plt.plot(t,y)
plt.ylim(-0.1,2)
plt.title("mixed ODE")
plt.legend(["x","y"])
plt.show()










