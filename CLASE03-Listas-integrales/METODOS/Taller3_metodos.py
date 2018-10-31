import numpy as np
from scipy import integrate
from scipy.integrate import quad, dblquad
import matplotlib.pyplot as plt
from sympy import *
from sys import argv



def function1(x,a,b):
    return np.exp(-a*x)*np.sin(b*x)


def function2(x,a,b):
    return (35*x**4-30*x**2+3)/8.0

def function_integral1(x,a,b):
    return -np.exp(-a*x)*(a*np.sin(b*x)+b*np.cos(b*x))/(a**2+b**2)

def function_integral2(x,a,b):
    return (7*x**5-10*x**3+3*x)/8.0



a=float(argv[1])#0.1
b=float(argv[2])#1
N=int(argv[3])#1000
Np=int(float(argv[4]))#1E6
seccion=int(argv[-1])


if(seccion==1):
    x=np.linspace(0,5*np.pi,N)
    xrand=np.random.rand(Np)*(max(x)-min(x))
    function=function1
    function_integral=function_integral1

elif(seccion==2):
    x=np.linspace(-1,1,N)
    xrand=2*(np.random.rand(Np)-0.5)*max(x)
    function=function2
    function_integral=function_integral2




aux=np.exp(-a*x)
plt.plot(x,function(x,a,b))
if(seccion==1):
    plt.plot(x,aux,"r--")
    plt.plot(x,-aux,"r--")
plt.grid()
plt.show()
plt.close()

EXACT_VALUE=function_integral(x[-1],a,b)-function_integral(x[0],a,b)
print("Exact value=", EXACT_VALUE)

# COMENZANDO LOS METODOS DE INTEGRACION

F=function
y=F(x,a,b)
dx=abs(x[1]-x[0])

#------------------------------Integracion por cuadrados------------------------------
suma_rec=sum(y)*dx
print("Rectangular method value=", suma_rec)

#-------------------Integracion por paralelogramos (Simpson)------------------------------
suma_par=0
for i in range(1,len(x)):
    suma_par+=(dx/6.0)*(F(x[i-1],a,b)+4*F((x[i-1]+x[i])/2,a,b) + F(x[i],a,b) )
print("integracion por Simpson",suma_par)

#------------------------------Integracion por valores trapz------------------------------
suma_trapz=0
for i in range(1,len(x)):
    suma_trapz+=dx*(F(x[i],a,b)+F(x[i-1],a,b))/2

print("integracion por trapezoides",suma_trapz)


#------------------------------Integracion por valores medio------------------------------
suma_mean=0
Dx=0
aux=[]
for i in range(len(y)):
    Dx+=dx #lenght of the interval
    aux.append(y[i])
    if(i<len(y)-1 and np.sign(y[i-1])!=np.sign(y[i])):
        suma_mean+=Dx*np.average(aux)
        aux=[]
        Dx=0
    elif(i==len(y)-1):
        suma_mean+=Dx*np.average(aux)


print("integracion por valores medios",suma_mean)


#------------------------------Integracion 2D montecarlo------------------------------


Fup=np.zeros(len(y))
Fdo=np.zeros(len(y))

for i in range(len(y)):
    if(y[i]>=0):
        Fup[i]=y[i]
    else:
        Fdo[i]=y[i]

plt.plot(x,Fup, label="Fup")
plt.plot(x,Fdo, label="Fdo")
plt.legend()
plt.show()

plt.close()

Areaup=(max(x)-min(x))*max(Fup)
Areado=(max(x)-min(x))*min(Fdo)

#xrand=2*(np.random.rand(Np)-0.5)*max(x)
#xrand=np.random.rand(Np)*(max(x)-min(x))
yrand_up=np.random.rand(Np)*(max(Fup))
yrand_do=np.random.rand(Np)*(min(Fdo))

dif_up=F(xrand,a,b)-yrand_up
dif_do=F(xrand,a,b)-yrand_do

bellow_up=np.where(dif_up>0)
bellow_do=np.where(dif_do<0)


plt.plot(x,function(x,a,b),"k--")
plt.scatter(xrand[bellow_up],yrand_up[bellow_up])
plt.scatter(xrand[bellow_do],yrand_do[bellow_do])
plt.show()
Area_MC=Areaup*(np.size(bellow_up)*1.0/np.size(xrand))+Areado*(np.size(bellow_do)*1.0/np.size(xrand))
print("integracion MC ",Area_MC)


#--------------------------Integracion por cuadraturas BONO 1------------------------------------------

func= lambda x: F(x,a,b)
RES_quad=quad(func,min(x),max(x))
print("integracion quad ",RES_quad[0])

#--------------------------Integracion por cuadraturas BONO 1------------------------------------------
x=Symbol("x")
a=Symbol("a")
b=Symbol("b")

if(seccion==1):
    Integral=integrate(exp(-0.1*x)*sin(1*x),x)
elif(seccion==2):
    Integral=integrate((35*x**4-30*x**2+3)/8.0,x)






print("\n")
print("------------Errores de cada metodo---------------")
if(seccion==1):
    print("Rectangulos=",100*abs(suma_rec-EXACT_VALUE)/EXACT_VALUE)
    print("Valor medio=",100*abs(suma_mean-EXACT_VALUE)/EXACT_VALUE)
    print("Trapezoides=",100*abs(suma_trapz-EXACT_VALUE)/EXACT_VALUE)
    print("Simpson=",100*abs(suma_par-EXACT_VALUE)/EXACT_VALUE)
    print("MC=",100*abs(Area_MC-EXACT_VALUE)/EXACT_VALUE)
print("quad=",RES_quad[1])#round(100*abs(RES_quad-EXACT_VALUE)/EXACT_VALUE,30))
print(Integral)



