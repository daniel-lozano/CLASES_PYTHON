import numpy as np
import matplotlib.pyplot as plt


class punto():

    def __init__(self, x0=0, y0=0):
        self.x = x0
        self.y = y0
        self.theta=0
        self.r=np.sqrt(self.x**2+self.y**2)
	


    def move(self,x,y):
        self.x += x
        self.y += y
        
        if( (self.x>0 and self.y>0) or ((self.x>0 and self.y<0))):#-pi/2 a pi/2
            self.theta=np.arctan(y/x)
        else:#pi/2 a -pi/2
            self.theta=np.arctan(y/x)+np.pi
                
        
        self.r=np.sqrt(self.x**2+self.y**2)

    def print_object(self):
        print("x", self.x)
        print("y", self.y)
        print("distance", self.r)


Pasos=0
x=[]
y=[]

particula=punto()

x.append(particula.x)
y.append(particula.y)

while particula.r< 10:
        stepx=np.random.uniform(-1,1)
        stepy=np.random.uniform(-1,1)
        Pasos+=1
        particula.move(stepx,stepy)
        x.append(particula.x)
        y.append(particula.y)



print(Pasos)
print(particula.r)

plt.plot(x,y,"k-o",linewidth=0.5)
plt.show()
plt.close()

Np=1000
N=500
theta=[]
r=[]
for j in range(Np):
    particula=punto()
    for i in range(N):
        stepx=2*(0.5-np.random.rand())
        stepy=2*(0.5-np.random.rand())
        Pasos+=1
        particula.move(stepx,stepy)
        x.append(particula.x)
        y.append(particula.y)
    
    r.append(particula.r)
    theta.append(particula.theta)





plt.subplot(111,projection="polar")
plt.scatter(theta,r)
plt.show()
plt.close()










	

