import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(x)

N=100
x=np.linspace(0,np.pi*2,N)
dx=x[1]-x[0]
fp=np.cos(x)

x1=[]
F_p1=[]
for i in range(len(x)-1):
	x1.append(x[i])
	F_p1.append( (1/dx) * (f(x[i+1])- f(x[i]))   )

#sin for-----------------

x2=x[:-1]
F_p2=(1/dx)*( f(x[1:]) - f(x[:-1]) )

plt.plot(x,fp,label="exact")
plt.plot(x1,F_p1,label="m1")
plt.plot(x2,F_p2,label="m2")
plt.legend()
plt.show()




