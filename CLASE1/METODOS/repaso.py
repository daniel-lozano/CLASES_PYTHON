#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from sys import argv

#Creando la clase-------------------------------------------------------------------------
class numero(object):
    "describe el movimiento de una particula en un campo magnetico"
    def __init__(self,num0):
        self.num=num0
    
    def primo(self):

	pri=False

	for i in range(2,self.num-1):
		if(self.num/(i*1.0) == self.num/i ):
			pri=True 	
        self.primo=pri

    def C_factorial_val(self):
        a=1.0
        for i in range(1,self.num+1):
            a=a*i
        self.factorial_val=a

    def C_factorial_vec(self):
        a=np.zeros(self.num+1)
        a[0]=1
        for i in range(1,self.num+1):
            a[i]=a[i-1]*i
        self.factorial_vec=a
    
   
       
#Usando la clase-------------------------------------------------------------------------

NUMERO=int(argv[1])
x=np.zeros(NUMERO+1)
for i in range(len(x)):
    x[i]=i

prueba=numero(NUMERO)
prueba.C_factorial_val()
prueba.C_factorial_vec()

print(prueba.num)
print(prueba.factorial_val)
print(prueba.factorial_vec)
print(x)

plt.plot(x,prueba.factorial_vec,"-o")
plt.show()





