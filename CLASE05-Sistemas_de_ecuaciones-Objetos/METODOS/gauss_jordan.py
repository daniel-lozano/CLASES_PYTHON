import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import *
from scipy.linalg import expm,inv

def Solve_system(A,b):
	M=np.float_(A)
	I=np.eye(len(b))
	x=np.float_(b)
	
	for i in range(len(x)):
	#Primero se normalizan los pibotes
		a=M[i,i]
		M[i,:]=M[i,:]/a
		I[i,:]=I[i,:]/a
		x[i]=x[i]/a
		#Se empieza a crear triangular superior
		for j in range(i+1,len(x)):
			multiple=M[j,i]
			I[j,:]=I[j,:]-multiple*I[i,:]
			M[j,:]=M[j,:]-multiple*M[i,:] #Se elimina los valores abajo del pibote
			x[j]=x[j]-multiple*x[i]#Se halla la solucion
	
	for i in range(len(x)-1,-1,-1):
		for j in range(i+1,len(x)):
			multiple=M[i,j]
			x[i]=x[i]-multiple*x[j]
			

	return I,x


A=[[1,2,3],[-1,1,2],[1,2,2]]
b=[1,2,1]

inverse=Solve_system(np.copy(A),np.copy(b))
print("Con reduccion gaussiana=",inverse[1],np.matmul(A,inverse[1]),b)
print("Con metodos de linalg=",solve(A,b),np.matmul(A,solve(A,b)),b)


