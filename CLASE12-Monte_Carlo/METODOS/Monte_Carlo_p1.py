import numpy as np
import matplotlib.pyplot as plt

#Primera Parte
L=200
x=np.linspace(-2,2,L)

N=2000

def funcion(x,a,b):
    return a*x +b*x**2-x**3

def chi2(y_ob,y_prediction):
    return sum((y_ob-y_prediction)**2)


#Definiendo valores iniciales para los parametros
param1=[1]
param2=[1]
chi=[]

a_teo=2.
b_teo=0.5

y_ob=funcion(x,a_teo,b_teo)+np.random.uniform(-0.2,0.2,L)
plt.scatter(x,y_ob,s=15)
plt.show()

FILE=open("datos.txt","w")
for i in range(L):
    FILE.write(str(x[i])+" " + str(y_ob[i]) +"\n")
FILE.close()

chi.append(chi2(y_ob,funcion(x,param1[-1],param2[-1])))

for i in range(N):
    
    avance_a=np.random.uniform(-0.5,0.5)
    avance_b=np.random.uniform(-0.5,0.5)
    
    #mirando el avance en el espacio de parametros
    pa1=param1[-1]+avance_a
    pa0=param1[-1]
    
    pb1=param2[-1]+avance_b
    pb0=param2[-1]
    
    new_prediction=funcion(x,pa1,pb1)
    old_prediction=funcion(x,pa0,pb0)
    
    #comparacion, si >1 es mejor la nueva prediccion
    
    alpha=chi2(y_ob,old_prediction)/chi2(y_ob,new_prediction)
    
    #Valor auxiliar
    beta=np.random.rand()
    
    
    if(alpha>1):# Mejor el nuevo
        param1.append(pa1)
        param2.append(pb1)
    
    
    else:   #Gamble!
        if(beta<alpha):
            param1.append(pa1)
            param2.append(pb1)

        else:
            param1.append(pa0)
            param2.append(pb0)
    chi.append(chi2(y_ob,funcion(x,param1[-1],param2[-1])))


print(param1[-1],param2[-1])
plt.scatter(param1,param2)
plt.xlabel("$ a $")
plt.ylabel("$ b $")
plt.show()

index=np.argmin(chi)
print(param1[index],param2[index])
print("Parametros teoricos")
print(a_teo,b_teo)


plt.plot(x,funcion(x,param1[index],param2[index]),"r--")
plt.scatter(x,y_ob,s=15)
plt.xlabel("$ x_{ob} $")
plt.ylabel("$ y(x) $")
plt.show()


















