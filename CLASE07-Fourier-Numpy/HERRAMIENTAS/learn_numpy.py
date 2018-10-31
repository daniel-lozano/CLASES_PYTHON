#! /bin/python2.7.1

import numpy as np
import matplotlib.pyplot as plt

#Punto 1: Usando arreglos de numpy desarrolle una funcion que de como resultado la suma (el producto) de todos los numeros enteros hasta un numero maximo N,

def sumaN(N):
    numero=int(N)
    lista=[]
    for i in range(1,N+1):
        lista.append(i)
    return sum(np.array(lista))

def multN(N):
    numero=int(N)
    lista=[]
    for i in range(1,N+1):
        lista.append(i)
    return np.prod(np.array(lista))

num=10
lista1=np.zeros(num)
lista2=np.zeros(num)
x=np.zeros(num)

for i in range(num):
    x[i]=i+1
    lista1[i]=sumaN(i+1)
    lista2[i]=multN(i+1)

#print(lista1, lista2)
plt.subplot(211)
plt.title("Suma")
plt.semilogy(x,lista1)

plt.subplot(212)
plt.title("Multiplicacion")
plt.semilogy(x,lista2)
plt.show()

#Punto 2: Campo electrico de dos cargas

def campo(xx,yy,xo1,xo2,yo1,yo2):
    return (1./((xx-xo1)**2+(yy-yo1)**2)+1./((xx-xo2)**2+(yy-yo2)**2))

yy,xx=np.mgrid[-3:3:0.1,-3:3:0.1]
xo1=1.01
xo2=-xo1
yo1=0.
yo2=0.
zz1=(campo(xx,yy,xo1,xo2,yo1,yo2))

print("Maximo=",zz1.max())
print(np.where(zz1==zz1.max()))
print("Minimo=",zz1.min())
print(np.where(zz1==zz1.min()))


im1=plt.imshow(np.arctan(zz1),cmap="gist_heat")
plt.colorbar(im1,orientation="vertical")
plt.show()


plano=zz1[30,:]
x=xx[30,:]
plt.semilogy(x,plano)
plt.show()

##punto 2b
yy,xx=np.mgrid[-15:15:0.1,-15:15:0.1]

def proba(xx,yy):
    return np.cos(np.sqrt(xx**2+yy**2))*np.exp(-0.05*np.sqrt(xx**2+yy**2))

zz2=proba(xx,yy)
im2=plt.imshow(zz2,cmap="gist_heat")
plt.colorbar(im2,orientation="vertical")
#plt.show()

print(zz2.max())
print(np.where(zz2==zz2.max()))
print(zz2.min())
print(np.where(zz2==zz2.min()))

Px=np.where(zz2==zz2.max())[0]
Py=np.where(zz2==zz2.max())[1]
px=np.where(zz2==zz2.min())[0]
py=np.where(zz2==zz2.min())[1]



plt.scatter(px,py,c="g")
plt.scatter(Px,Py,c="c")
plt.show()

levels = np.linspace(0,np.pi/2,40)
plt.contour(xx,yy,np.arctan(campo(xx,yy,xo1,xo2,yo1,yo2)),levels=levels)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.show()












