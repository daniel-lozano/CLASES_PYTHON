import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import argv 

N=int(argv[-1])

pasos=1000

Alcance=np.zeros(N)

for i in range(N):
	suma=0

	for j in range(pasos):
		variable=np.random.random()
		if(variable>=0.5):
			suma+=1
		else:
			suma-=1
	Alcance[i]=suma

plt.hist(Alcance,bins=int(N*0.1))
plt.show()

x=np.zeros(N)
y=np.zeros(N)
z=np.zeros(N)

for i in range(1,N):
	
	variablex=np.random.random()
	variabley=np.random.random()
	variablez=np.random.random()

	if(variablex>=0.5):
		x[i]=x[i-1]+1
	elif(variablex<0.5):
		x[i]=x[i-1]-1
	
	if(variabley>=0.5):
		y[i]=y[i-1]+1
	elif(variabley<0.5):
		y[i]=y[i-1]-1

	if(variablez>=0.5):
		z[i]=z[i-1]+1
	elif(variablez<0.5):
		z[i]=z[i-1]-1

#Graficando 3D
fig=plt.figure()
#ax=plt.axes(projection='3d')
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z)
plt.show()	


