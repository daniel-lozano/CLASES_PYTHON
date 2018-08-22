import numpy as np
import matplotlib.pyplot as plt
from numpy import random

class punto():

    def __init__(self, x0=0, y0=0):
        self.x = x0
        self.y = y0
        self.r=np.sqrt(self.x**2+self.y**2)
	


    def move(self,x,y):
        self.x += x
        self.y += y
        self.r=np.sqrt(self.x**2+self.y**2)

    def print_object(self):
        print("x", self.x)
        print("y", self.y)
        print("distance", self.r)

particula=punto()
Pasos=0
f=open("caminata.txt","w")
f.write(str(particula.x)+" "+str(particula.y)+" "+str(Pasos)+"\n")

while particula.r< 10:
	var=random.rand()
	stepx=2*(0.5-random.rand())
	stepy=2*(0.5-random.rand())
	Pasos+=1
	if(var<0.5):
	    particula.move(stepx,stepy)

	f.write(str(particula.x)+" "+str(particula.y)+" "+str(Pasos)+"\n")


print(Pasos)
print(particula.r)
f.close()

N=5000 #Numero de intentos
N_p=100
R=np.zeros(N)

for i in range(len(R)):
	p=punto()

	for j in range(N_p):
		paso=2*(0.5-random.rand())
		p.move(paso,0)	
	R[i]=p.x

plt.hist(R,bins=100)
plt.show()
plt.close()








	

