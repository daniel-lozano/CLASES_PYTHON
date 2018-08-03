#!/usr/bin/python
import matplotlib.pyplot as plt


#creando la clase en python ---------------------------------------------------

class Balon: #definiendo una clase
    "descripcion de la clase y su uso"
    g=9.8  #m/s^2  # variable universal en la clase
    
    def __init__(self,y0,Vy0,m0):

        self.y=y0 # se utiliza el comando self para referirse a la clase
        self.Vy=Vy0
        self.m=m0
    
    def calcula_fuerza(self):
        self.Fy=-self.m*Balon.g # nuevamente llamamos la masa utilizando self, pues es propia de la clase la variable universal se llama <clase>.<variable>
    
    def muevete(self,dt):
        self.y+=self.Vy*dt
        self.Vy+=dt*self.Fy/self.m
        
    def imprime(self,t):
        print t,self.y

    def dar_variables(self):
        return [self.y,self.Vy]

#usando la clase en python ---------------------------------------------------
pelota=Balon(0.0,4.0,0.453)
pelota.calcula_fuerza()

t=0.0
dt=0.01
y=[]
Vy=[]
T=[]
while t<1.0:
    
    pelota.imprime(t)
    #print t,getattr(pelota,"y"),"usando getattr"
    pelota.muevete(dt)
    T.append(t)
    y.append(pelota.dar_variables()[0])
    Vy.append(pelota.dar_variables()[1])
    t+=dt


'''
plt.scatter(T,y,label="$  y(t) $")
plt.plot(T,Vy,label="$V_y(t) $")
plt.legend(loc=3)
plt.show()

plt.close
'''



