import numpy as np
import matplotlib.pyplot as plt

#Primer punto

x=np.linspace(0,2*np.pi,1000)

def func(x):
    return np.sin(x)*np.exp(-0.1*x)

def distribucion(x):
    return np.exp(-(x-5.)**2/16.)

def chi2(yt,ye):
    return sum((yt-ye)**2)

y=func(x)


plt.plot(x,y)
plt.grid()
plt.xlim(0,2*np.pi)
plt.ylim(-1,1)
plt.show()

N=10000
xr=np.random.uniform(0,2*np.pi,N)
yr1=np.random.uniform(0,1,N)
yr2=np.random.uniform(-1,0,N)

index1=np.where((func(xr)>yr1))
index2=np.where((func(xr)<yr2))

print len(index1[0]),len(index2[0])

plt.scatter(xr,yr1)
plt.scatter(xr,yr2)
plt.scatter(xr[index1],yr1[index1])
plt.scatter(xr[index2],yr2[index2])
plt.show()

Area_sup=(2.*np.pi*len(index1))/N
Area_inf=(2.*np.pi*len(index2))/N
Area_tot=Area_sup-Area_inf
print Area_tot

#Segundo punto

#N=20000 #numero de puntos
#
#puntos=[]
#puntos.append(np.random.uniform(0,10))
#
#for i in range(N):
#    p_rand=np.random.uniform(-5,15)
#    p0=distribucion(puntos[-1])
#    p1=distribucion(p_rand+p0)
#    
#    alpha=p1/p0
#    if(alpha>1):
#        puntos.append(p_rand)
#    else:
#        beta=np.random.rand()
#        if(beta>alpha):
#            puntos.append(puntos[-1])
#        else:
#            puntos.append(p_rand)
#print len(puntos)
#plt.hist(puntos,bins=50)
##plt.plot(p_rand)
#plt.show()

#Estimacion de parametros
N=2000

def funcion(x,a):
    return a*x

x=np.linspace(0,5,100)
param=[1]
a_teo=2.
y_ob=funcion(x,a_teo)+np.random.uniform(-0.2,0.2,100)
plt.scatter(x,y_ob,s=5)
plt.show()

for i in range(N):
    avance=np.random.uniform(-1,1)
    p1=param[-1]+avance
    p0=param[-1]
    
    new_prediction=funcion(x,p1)
    old_prediction=funcion(x,p0)
    
    alpha=chi2(y_ob,old_prediction)/chi2(y_ob,new_prediction)
    beta=np.random.rand()
    if(alpha>1):
        param.append(p1)
    else:
        if(beta<alpha):
            param.append(p1)
        else:
            param.append(p0)

print(param[-1])
plt.plot(param)
plt.show()
















