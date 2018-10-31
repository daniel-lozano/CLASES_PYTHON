import numpy as np
import matplotlib.pyplot as plt

def f(t,A,w,b):
	return A*np.cos(t*w)*np.exp(-b*t)
def F_prime_exact(t,A,w,b):
    return -A*w*np.sin(t*w)*np.exp(-b*t)-A*b*np.cos(t*w)*np.exp(-b*t)
def F_prime_prime_exact(t,A,w,b):
    return -A*pow(w,2)*np.cos(t*w)*np.exp(-b*t) +b*A*w*np.sin(t*w)*np.exp(-b*t) +A*w*b*np.sin(t*w)*np.exp(-b*t) +A*pow(b,2)*np.cos(t*w)*np.exp(-b*t)

N=100
A=1
w=1
b=0.1
t=np.linspace(0,np.pi*4,N)
dt=t[1]-t[0]
Ft=f(t,A,w,b)
Ft_p_exact=F_prime_exact(t,A,w,b)


#Derivada por diferencia hacia adelante
Ft_p_f=(1.0/dt)*(Ft[1:]-Ft[0:-1])

#Derivada por diferencia central
Ft_p_c=[]
for i in range(1,len(t)-1):
    Ft_p_c.append((0.5/dt)*(Ft[i+1]-Ft[i-1]))



plt.plot(t,Ft,label="Original")
plt.plot(t,Ft_p_exact,label="Exact")
plt.plot(t[1:],Ft_p_f,label="forward")
plt.plot(t[1:-1],Ft_p_c,label="central")
plt.title("$ \mathrm{Primera\ derivada} $")
plt.grid()
plt.legend()
plt.show()

#------------------mirando las diferencias---------
plt.semilogy(t[1:],abs(Ft_p_f-Ft_p_exact[1:]),label="forward")
plt.semilogy(t[1:-1],abs(Ft_p_c-Ft_p_exact[1:-1]),label="central")
plt.title("$ \mathrm{Primera\ derivada} $")
plt.grid()
plt.legend()
plt.show()
plt.close()


#------------------Segunda Derivada---------

Ft_p_p_exact=F_prime_prime_exact(t,A,w,b)
Ft_p_p=[]

for i in range(1,len(Ft)-1):
    Ft_p_p.append((Ft[i+1]-2*Ft[i]+Ft[i-1])/dt**2)
plt.plot(t,Ft_p_p_exact,"r",linewidth=2,label="exact")
plt.plot(t[1:-1],Ft_p_p,"k--",label="numerical")
plt.title("$ \mathrm{Segunda\ derivada} $")
plt.legend()
plt.grid()
plt.show()





