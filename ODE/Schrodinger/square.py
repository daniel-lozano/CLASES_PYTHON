import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar

m= 1e-27
E= 0.5

def numerov_step(psi_1,psi_2,k1,k2,k3,h):
    #k1=k_(n-1), k2=k_n, k3=k_(n+1)
    #psi_1 = psi_(n-1) and psi_2=psi_n
    m = 2*(1-5/12. * h**2 * k2**2)*psi_2
    n = (1+1/12.*h**2*k1**2)*psi_1
    o = 1 + 1/12. *h**2 *k3**2
    return (m-n)/o

def numerov(N,x0,xE,a):
    x,dx = np.linspace(x0,xE,N+1,retstep=True)
    
    def V(x,a):
        if (np.abs(x)<a):
            return 1
        else:
            return 0

    k = np.zeros(N+1)
    for i in range(len(k)):
        k[i] = 2*m*(E-V(x[i],a))/hbar**2
    
    psi= np.zeros(N+1)
    psi[0]=0
    psi[1]=0.1
    
    for j in np.arange(2,N):
        psi[j+1]= numerov_step(psi[j-2],psi[j-1],k[j-2],k[j-1],k[j],dx)
    
    return psi

x0 =-10
xE = 10
N =1000

psi=numerov(N,x0,xE,3)

x = np.linspace(x0,xE,N+1)

plt.figure()
plt.plot(x,psi)
plt.show()
