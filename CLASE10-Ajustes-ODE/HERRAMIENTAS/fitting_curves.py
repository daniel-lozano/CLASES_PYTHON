import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



def func1(t,a1,w1):
    return a1*np.sin(w1*t)/t

def func2(t,a2,w2):
    return a2*np.arctan(t)*np.sin(w2*t)

def fun_suma1(t,a,w):
    return a*np.sin(w*t)/t+0.5*t

def fun_suma2(t,a,w):
    return a*np.arctan(t)*np.sin(w*t)+t

def chi_sqrt(y,yp):
    return np.sum((y-yp)**2)

frequencies=[5,3]
amplitudes=[10,30]

N=500
t1=np.random.uniform(0,7,N)
t2=np.random.uniform(0,2*np.pi/6,N)

y_1=np.zeros(N)
y_2=np.zeros(N)

ruido1=np.random.normal(0,2 ,N)#(np.random.rand(N)*0.5+1)
ruido2=np.random.normal(0,0.5,N)

y_1=ruido1+fun_suma1(t1,amplitudes[0],frequencies[0])
y_2=ruido2+func2(t2,amplitudes[1],frequencies[1])

file1=open("datos_s1.txt","w")
file2=open("datos_s2.txt","w")

for i in range(len(t1)):
    file1.write(str(t1[i])+" "+str(y_1[i])+"\n")
    file2.write(str(t2[i])+" "+str(y_2[i])+"\n")
file1.close()
file2.close()

DATOS1 =np.loadtxt("datos_s1.txt")
DATOS2 =np.loadtxt("datos_s2.txt")

t1=DATOS1[:,0]
y_t1=DATOS1[:,1]
t2=DATOS2[:,0]
y_t2=DATOS2[:,1]
plt.subplot(211)
plt.scatter(t1,y_t1,s=5,label="datos seccion 1")
plt.subplot(212)
plt.scatter(t2,y_t2,s=5,label="datos seccion 2")
plt.legend()
plt.show()


a1,w1=curve_fit(func1,t1,y_t1)[0]
a2,w2=curve_fit(func2,t2,y_t2,p0=[50,2])[0]

a1p,w1p=curve_fit(fun_suma1 ,t1,y_t1)[0]
a2p,w2p=curve_fit(fun_suma2,t2,y_t2)[0]

print("a1=",amplitudes[0])
print("w1=",frequencies[0])
print("a2=",amplitudes[1])
print("w2=",frequencies[1])
print("-------------------------------------------------")
print("                     Seccion 1")
print("-------------------------------------------------")
print("a1=",a1,abs(a1-amplitudes[0])/amplitudes[0])
print("w1=",w1,abs(w1-frequencies[0])/frequencies[0])
print("a1p=",a1p,abs(a1p-amplitudes[0])/amplitudes[0])
print("w1p=",w1p,abs(w1p-frequencies[0])/frequencies[0])


print("-------------------------------------------------")
print("                     Seccion 2")
print("-------------------------------------------------")
print("a2=",a2,abs(a2-amplitudes[1])/amplitudes[1])
print("w2=",w2,abs(w2-frequencies[1])/frequencies[1])
print("a2p=",a2p,abs(a2p-amplitudes[1])/amplitudes[1])
print("w2p=",w2p,abs(w2p-frequencies[1])/frequencies[1])




y_opt1=func1(t1,a1,w1)
y_opt2=func2(t2,a2,w2)

y_opt1p=fun_suma1(t1,a1p,w1p)
y_opt2p=fun_suma2(t2,a2p,w2p)



plt.subplot(211)
plt.scatter(t1,y_t1,label="real data")
plt.scatter(t1,y_opt1,s=5,c="r",label="sin t")
plt.scatter(t1,y_opt1p,s=5,c="g",label="con t")
plt.legend()
plt.subplot(212)
plt.scatter(t2,y_t2,label="real data")
plt.scatter(t2,y_opt2,s=5,c="r",label="sin t")
plt.scatter(t2,y_opt2p,s=5,c="g",label="con t")
plt.legend()
plt.show()

print("-------------------------------------------------")
print("                     Seccion 1")
print("-------------------------------------------------")
print("chi_sqr_1",chi_sqrt(y_t1,y_opt1)/N)
print("chi_sqr_1p",chi_sqrt(y_t1,y_opt1p)/N,"Esta es la solucion !")

print("-------------------------------------------------")
print("                     Seccion 2")
print("-------------------------------------------------")
print("chi_sqr_2",chi_sqrt(y_t2,y_opt2)/N,"Esta es la solucion !")
print("chi_sqr_2p",chi_sqrt(y_t2,y_opt2p)/N)

