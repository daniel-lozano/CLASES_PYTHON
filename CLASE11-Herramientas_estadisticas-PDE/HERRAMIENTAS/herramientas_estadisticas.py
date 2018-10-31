import numpy as np
import math as m
import matplotlib.pyplot as plt
lam=10
N=1000

Poisson=np.random.poisson(lam,N)
Poisson=Poisson-np.mean(Poisson)*np.ones(N)
Gauss=np.random.normal(0,3,N)
Uniform=np.random.uniform(-10,10,N)


def standar_dev(lista,mean):
    return np.sqrt(sum((mean-lista)**2)/(len(lista)-1))

def division(d,lista):
    contador=0
    for i in lista:
        if(i<d):
            contador+=1.
    return (contador/len(lista))

def punto_medio(lista):
    LIST=np.sort(lista)
    mid=len(lista)//2
    if(len(lista)/2-len(lista)//2==0):
        return (LIST[mid]+LIST[mid+1])/2
    return LIST[mid]


plt.subplot(131)
plt.hist(Poisson,bins=20,label="Poisson")
plt.legend()
plt.subplot(132)
plt.hist(Uniform,bins=20,alpha=1,label="Uniform")
plt.legend()
plt.subplot(133)
plt.hist(Gauss,bins=20,alpha=1,label="Gauss")
plt.legend()
plt.show()

meanP=np.mean(Poisson)
meanG=np.mean(Gauss)
meanU=np.mean(Uniform)

medianP=np.median(Poisson)
medianG=np.median(Gauss)
medianU=np.median(Uniform)


print "-----------------------------------"
print "                  Mean   "
print "-----------------------------------"
print "meanP=", meanP
print "meanG=", meanG
print "meanU=", meanU


print "-----------------------------------"
print "                  Median   "
print "-----------------------------------"
print "medianP=", medianP
print "medianG=", medianG
print "medianU=", medianU


print "-----------------------------------"
print "                  std   "
print "-----------------------------------"

print standar_dev(Gauss,meanG),np.std(Gauss)
print "Error=",abs(standar_dev(Gauss,meanG)-np.std(Gauss))/np.std(Gauss),"\n"

print standar_dev(Poisson,meanP),np.std(Poisson)
print "Error=",abs(standar_dev(Poisson,meanP)-np.std(Poisson))/np.std(Poisson),"\n"

print standar_dev(Uniform,meanU),np.std(Uniform)
print "Error=",abs(standar_dev(Uniform,meanU)-np.std(Uniform))/np.std(Uniform),"\n"

#Cuantos punto hay a cada lado?

print "-----------------------------------"
print "   Cuantos punto hay a cada lado?  "
print "-----------------------------------"



print "\nMEAN\n"
print "Gauss",division(meanG,Gauss)
print "Poisson",division(meanP,Poisson)
print "Uniform",division(meanU,Uniform)

print "\nMEDIAN\n"
print "Gauss",division(medianG,Gauss)
print "Poisson",division(medianP,Poisson)
print "Uniform",division(medianU,Uniform)

print "-----------------------------------"
print "   Caminata aleatoria  "
print "-----------------------------------"

A_std=[]
x=[]
N=1000
suma=0
x.append(suma)
for i in range(N):
    suma+=np.random.uniform(-1,1)
    x.append(suma)
    A_std.append(np.std(x))
plt.plot(A_std)
plt.show()

X=[]
N=1000
for i in range(N):
    suma=0
    for j in range(N):
        suma+=np.random.uniform(-1,1)
    X.append(suma)
plt.hist(X,bins=40)
plt.show()








