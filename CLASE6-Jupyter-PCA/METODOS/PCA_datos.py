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

FILE=open("datos.csv","r")
lineas=FILE.readlines()
DATOS=[]

for linea in lineas:
    variable=list(map(float,linea.split(",")[1:]))
    variable-=np.mean(variable)
    variable=variable/np.sqrt(np.var(variable))
    DATOS.append(variable)


print(np.shape(DATOS))

M_cov=np.cov(DATOS)
val,eig=eig(M_cov)
print(eig)

#
#origin=[0],[0],[0]
#V1=eig[0][0],eig[0][1],eig[0][2]
#V2=eig[1][0],eig[1][1],eig[1][2]
#V3=eig[2][0],eig[2][1],eig[2][2]
#
#ax.quiver(*origin,*V1,color="r",length=7,linewidth=2)
#ax.quiver(*origin,*V2,color="c",length=7,linewidth=2)
#ax.quiver(*origin,*V3,color="g",length=7,linewidth=2)
#plt.show()
#
#MAT1=np.zeros(np.shape(DATOS))
#
#for i in range(len(DATOS[0,:])):
#    MAT1[:,i]=eig[0]*np.dot(eig[0],DATOS[:,i])+eig[1]*np.dot(eig[1],DATOS[:,i])
#
#xn=MAT1[0,:]
#yn=MAT1[1,:]
#zn=MAT1[2,:]
#
#fig=plt.figure()
#ax=fig.add_subplot(111,projection="3d",alpha=0.01)
#ax.scatter(xn,yn,zn)
#ax.quiver(*origin,*V1,color="r",length=3,linewidth=2)
#ax.quiver(*origin,*V2,color="k",length=3,linewidth=2)
#ax.quiver(*origin,*V3,color="b",length=3,linewidth=2)
#plt.show()
#
#MAT2=np.zeros(np.shape(DATOS))
#
#for i in range(len(DATOS[0,:])):
#    MAT2[:,i]=eig[1]*np.dot(eig[1],DATOS[:,i])+eig[2]*np.dot(eig[2],DATOS[:,i])
#
#xn=MAT2[0,:]
#yn=MAT2[1,:]
#zn=MAT2[2,:]
#
#fig=plt.figure()
#ax=fig.add_subplot(111,projection="3d",alpha=0.01)
#ax.scatter(xn,yn,zn)
#ax.quiver(*origin,*V1,color="r",length=3,linewidth=2)
#ax.quiver(*origin,*V2,color="k",length=3,linewidth=2)
#ax.quiver(*origin,*V3,color="b",length=3,linewidth=2)
#plt.show()




