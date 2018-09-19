#Paquetes Basicos------------------------------
import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt

#Para el manejo de algebra lineal---------------
from numpy.linalg import *
from scipy.linalg import expm,inv

#Para los plots 3D -----------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N=1000

x=uniform(0,9,N)
ruido=uniform(-2,2,N)#+np.sin(x1)
y=x+ruido*np.exp(-0.1*(x-5)**2)
z=x+y+uniform(-3,3,N)*np.exp(0.05*(-(x-np.mean(x))**2-(y-np.mean(y))**2))

#Changing data

meanx=np.mean(x)
meany=np.mean(y)
meanz=np.mean(z)

xn=(x-meanx)
yn=(y-meany)
zn=(z-meanz)

xn=xn/np.sqrt(np.var(xn))
yn=yn/np.sqrt(np.var(yn))
zn=zn/np.sqrt(np.var(zn))

#plt.scatter(xn,yn)
#plt.title("Datos centrados")
#plt.xlabel("x")
#plt.ylabel("y")

fig=plt.figure()
ax=fig.add_subplot(111,projection="3d",alpha=0.01)
ax.scatter(xn,yn,zn)



DATOS=np.array([xn,yn,zn])

print("varx",np.var(xn))
print("vary",np.var(yn))
print("varz",np.var(zn))
print("covx",np.cov(xn))
print("covy",np.cov(yn))
print("covz",np.cov(zn))
print("Covariance Matrix")
print(np.cov(DATOS))

M_cov=np.cov(DATOS)
val,eig=eig(M_cov)
print(eig)
print("eigen values",val)


origin=[0],[0],[0]
V1=eig[0][0],eig[0][1],eig[0][2]
V2=eig[1][0],eig[1][1],eig[1][2]
V3=eig[2][0],eig[2][1],eig[2][2]

ax.quiver(*origin,*V1,color="r",length=7,linewidth=2)
ax.quiver(*origin,*V2,color="c",length=7,linewidth=2)
ax.quiver(*origin,*V3,color="g",length=7,linewidth=2)
plt.show()

MAT1=np.zeros(np.shape(DATOS))
xp=np.zeros(N)
yp=np.zeros(N)

for i in range(len(DATOS[0,:])):
    MAT1[:,i]=eig[0]*np.dot(eig[0],DATOS[:,i])/np.dot(eig[0],eig[0])+eig[1]*np.dot(eig[1],DATOS[:,i])/np.dot(eig[1],eig[1])
    xp[i]=np.dot(eig[0],DATOS[:,i])/np.dot(eig[0],eig[0])
    yp[i]=np.dot(eig[1],DATOS[:,i])/np.dot(eig[1],eig[1])


xn=MAT1[0,:]
yn=MAT1[1,:]
zn=MAT1[2,:]

plt.scatter(xp,yp)
plt.title("1 vs 2")
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111,projection="3d",alpha=0.01)
ax.scatter(xn,yn,zn)
ax.quiver(*origin,*V1,color="r",length=3,linewidth=2)
ax.quiver(*origin,*V2,color="k",length=3,linewidth=2)
ax.quiver(*origin,*V3,color="b",length=3,linewidth=2)
plt.show()

MAT2=np.zeros(np.shape(DATOS))

for i in range(len(DATOS[0,:])):
    MAT2[:,i]=eig[1]*np.dot(eig[1],DATOS[:,i])/np.dot(eig[1],eig[1])+eig[2]*np.dot(eig[2],DATOS[:,i])/np.dot(eig[2],eig[2])
    xp[i]=np.dot(eig[1],DATOS[:,i])/np.dot(eig[1],eig[1])
    yp[i]=np.dot(eig[2],DATOS[:,i])/np.dot(eig[2],eig[2])


xn=MAT2[0,:]
yn=MAT2[1,:]
zn=MAT2[2,:]

plt.scatter(xp,yp)
plt.title("2 vs 3")
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111,projection="3d",alpha=0.01)
ax.scatter(xn,yn,zn)
ax.quiver(*origin,*V1,color="r",length=3,linewidth=2)
ax.quiver(*origin,*V2,color="k",length=3,linewidth=2)
ax.quiver(*origin,*V3,color="b",length=3,linewidth=2)
plt.show()




