#!/usr/bin/python
import matplotlib.pyplot as plt
from sys import argv

#Creando la clase-------------------------------------------------------------------------
class particula(object):
    "describe el movimiento de una particula en un campo magnetico"
    def __init__(self,x0,y0,Vx0,Vy0,m0,q0):
        self.x=x0
        self.y=y0
        self.Vx=Vx0
        self.Vy=Vy0
        self.q=q0
        self.m=m0
    
    def CalcularFuerzaX(self,Bz,Ex):
        self.Fx=self.q*(self.Vy*Bz+Ex)

    def CalcularFuerzaY(self,Bz,Ey):
        self.Fy=self.q*(-self.Vx*Bz+Ey)
    
    def muevete(self,dt):
        self.y+=self.Vy*dt
        self.x+=self.Vx*dt
        self.Vx+=dt*self.Fx/self.m
        self.Vy+=dt*self.Fy/self.m
    def imprime(self):
        print self.x,self.y
#Usando la clase-------------------------------------------------------------------------

B=10.0
Ex=5.0
Ey=5.0
Q=-1.0
M=1.0
X0=2.0
Y0=0.0
VX0=0.0
VY0=5.0





partacula=particula(X0,X0,VX0,VY0,M,Q)
partacula.CalcularFuerzaX(B,Ex)
partacula.CalcularFuerzaY(B,Ey)

dt=float(argv[1])
t=0.0

X=[]
Y=[]
T=[]
while t<10.0:
    partacula.muevete(dt)
   
    partacula.CalcularFuerzaX(B,Ex)#actualizando fuerza x
    partacula.CalcularFuerzaY(B,Ey)#actualizando fuerza y
    
    X.append(getattr(partacula,"x"))
    Y.append(getattr(partacula,"y"))
    T.append(t)
    
    partacula.imprime()
    t+=dt

plt.scatter(X,Y,label="trayectoria",s=3)
plt.show()
plt.close()
'''
plt.scatter(T,Y,label="trayectoria en t")
plt.show()
plt.close()
'''





