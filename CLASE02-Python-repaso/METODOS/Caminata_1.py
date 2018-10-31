import numpy as np
import matplotlib.pyplot as plt


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
    
        stepx=2*(0.5-np.random.rand())
        stepy=2*(0.5-np.random.rand())
        Pasos+=1
        particula.move(stepx,stepy)
        f.write(str(particula.x)+" "+str(particula.y)+" "+str(Pasos)+"\n")


print(Pasos)
print(particula.r)
f.close()

'''-----------------LEYEDO---------------------'''


f=open("caminata.txt","r")
lines=f.readlines()
x=[]	
y=[]
var=[]

for line in lines:
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))
        var.append(np.var(x))



plt.plot(x,y,"k-o",linewidth=0.5)
plt.show()
plt.close()


plt.plot(var,"k-o",linewidth=0.5)
plt.show()
plt.close()








	

