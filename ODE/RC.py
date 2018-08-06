import numpy as np
from scipy.integrate import odeint #solve ODE equations
import matplotlib.pyplot as plt


q0=0
N=150
t=np.linspace(0,15,N)
R=1.0
C=1.0

def model(q,t):
    
    if(t<=5 or 10<=t<=15):
        V=10
    else:
        V=0
    dqdt=(1.0/R*C)*(-q+V)
    return dqdt


Q=odeint(model,q0,t)
V_A=np.ones(N)*10
V_A[51:]=0
V_A[101:]=10
#print(V_A)

def current(Q,t):
    Array=[]
    for i in range(N):
        Array.append((1.0/R*C)*(-Q[i]+V_A[i]))
    return Array
I= current(Q,t)

plt.plot(t,Q,"r")
plt.plot(t,I,"b--")
plt.ylabel([" $Q(t) $","$ I(t) $"])
#plt.ylabel("$Q(t)$")
plt.show()



