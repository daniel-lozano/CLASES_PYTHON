import numpy as np
import matplotlib.pyplot as plt
import funciones as f


#Primera Parte
L=200

x=np.linspace(1,10,L)
dx=x[1]-x[0]

y_0=0
yp_0=1
y=np.zeros(len(x))
yp=np.zeros(len(x))
y[0]=y_0
yp[0]=yp_0

N=2000

def funcion(x,y,yp,dx,a,b):
    return f.Soluciona(x,y,yp,dx,a,b)

def chi2(y_ob,y_prediction):
    return sum((y_ob-y_prediction)**2)



#Definiendo valores iniciales para los parametros
param1=[3.5]
param2=[-17]
chi=[]

b_teo=3.
c_teo=-15.

print(b_teo,c_teo)

y_ob=funcion(x,y,yp,dx,b_teo,c_teo)+np.random.uniform(-0.5,0.5,L)
plt.scatter(x,y_ob,s=2)
plt.xlabel("$x$")
plt.ylabel("$ y(x) $")
plt.show()

FILE=open("datos2.txt","w")
for i in range(L):
    FILE.write(str(x[i])+" " + str(y_ob[i]) +"\n")
FILE.close()

chi.append( chi2(y_ob,funcion(x,y,yp,dx,param1[-1],param2[-1])) )

for i in range(N):
    
    avance_b=np.random.uniform(-0.5,0.5)
    avance_c=np.random.uniform(-0.5,0.5)
    
    
    #mirando el avance en el espacio de parametros
    pb1=param1[-1]+avance_b
    pb0=param1[-1]
    
    pc1=param2[-1]+avance_c
    pc0=param2[-1]
    
    
    new_prediction=funcion(x,y,yp,dx,pb1,pc1)
    old_prediction=funcion(x,y,yp,dx,pb0,pc0)
    
    #comparacion, si >1 es mejor la nueva prediccion
    
    alpha=chi2(y_ob,old_prediction)/chi2(y_ob,new_prediction)
    
    #Valor auxiliar
    beta=np.random.rand()
    
    
    if(alpha>1):# Mejor el nuevo
        param1.append(pb1)
        param2.append(pc1)
    
    
    else:   #Gamble!
        if(beta<alpha):
            param1.append(pb1)
            param2.append(pc1)
        
        else:
            param1.append(pb0)
            param2.append(pc0)
    chi.append( chi2(y_ob,funcion(x,y,yp,dx,param1[-1],param2[-1])) )



plt.scatter(param1,param2)
plt.xlabel("b")
plt.ylabel("c")
plt.show()

index=np.argmin(chi)
print(param1[index],param2[index])

plt.title("$b="+"\mathrm{"+str(param1[index])+"},\ c="+"\mathrm{"+str(param2[index])+"}$")
plt.plot(x,funcion(x,y,yp,dx,param1[index],param2[index]),"r--",label="Sol. por MC",linewidth=2)
plt.scatter(x,y_ob,s=20,alpha=0.5,label="Datos exp.")
plt.xlabel("$x$",size=15)
plt.ylabel("$ y(x) $",size=15)
plt.show()


















