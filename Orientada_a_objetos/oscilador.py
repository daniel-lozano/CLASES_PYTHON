#!/usr/bin/python
import matplotlib.pyplot as plt
from sys import argv


#creando la clase en python ---------------------------------------------------

class resorte: #definiendo una clase
    "descripcion de la clase y su uso"
    #m/s^2  # variable universal en la clase
    
    def __init__(self,x0,Vx0,m0):
        self.x=x0 # se utiliza el comando self para referirse a la clase
        self.Vx=Vx0
        self.m=m0
    
    def calcula_fuerza(self,k):
        self.Fx=-k*self.x
    
    def Energias(self,k):
        self.Ep=0.5*k*self.x**2
        self.Ek=0.5*self.m*self.Vx**2
        
    def muevete(self,dt):
        self.x+=self.Vx*dt
        self.Vx+=dt*self.Fx/self.m
        
    def imprime(self,t):
        print t,self.x


#usando la clase en python ---------------------------------------------------
k=1.0

caja=resorte(0.0,4.0,0.453)
caja.calcula_fuerza(k)
caja.Energias(k)

t=0.0
dt=float(argv[1])
x=[]
Vx=[]
Ep=[]
Ek=[]
Et=[]
T=[]
while t<10.0:
    
    #caja.imprime(t)
    caja.muevete(dt)
    caja.calcula_fuerza(k)
    caja.Energias(k)
    T.append(t)
    
    
    
    x.append(getattr(caja,"x"))
    Vx.append(getattr(caja,"Vx"))
    Ep.append(getattr(caja,"Ep"))
    Ek.append(getattr(caja,"Ek"))
    Et.append(getattr(caja,"Ep")+getattr(caja,"Ek"))
    t+=dt



plt.plot(T,x,"r",label="$  x(t) $")
plt.plot(T,Vx,"b",label="$V_x(t) $")
plt.title("$x,V_x\ \mathrm{vs.}\ t.\ $")
plt.xlabel("$ t\ $")
plt.savefig("X_V_dt="+str(dt)+".png")
plt.legend(loc=3)
plt.show()
plt.close()

plt.plot(T,Ep,"r",label="$  E_p(t) $")
plt.plot(T,Ek,"b",label="$E_k(t) $")
plt.plot(T,Et,"k--",label="$E_t(t) $")
plt.title("$E_p,E_k\ \mathrm{vs.}\ t.\ $")
plt.ylabel("$ \mathrm{Energy} $")
plt.xlabel("$ t\ $")
plt.savefig("E_dt="+str(dt)+".png")
plt.legend(loc=3)
plt.show()
plt.close()




