#! /bin/python2.7.1

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft,fftfreq

#se computara una funcion en python que dependa de mas de una frecuencia, el espectro de estas deberia dar las frecuencias principales del programa

N=500
f1=40
f2=90
t=np.linspace(0,0.5,N)
T=t[1]-t[0]
y_t=np.sin(f1*2*np.pi*t)+ 0.5 * np.sin(f2*2*np.pi*t)



# a partir de la ecuacion hallada se debe hallar la transformada de la funcion y_t
Norm=1.0/N
y_f=fft(y_t)*Norm

f=np.linspace(0,1/T,len(y_t))#frecuencia es 1/T el tiempo men

print "len original", len(y_t),"len fourier",len(y_f),"len armada",len(f)

figure=plt.subplot(211)
plt.plot(t,y_t)
plt.xlabel("time")
plt.ylabel("Signal")

figure=plt.subplot(212)

plt.plot(f[:N//2],np.abs(y_f[:N//2]))#se esta tomando hasta l mitad pues para estas transformadas de funciones reales, se tiene una repeticion por complejos conjugados de los valores, el valor absoluto muestra solo los valores de las amplitudes
plt.xlabel("frecuencias")
plt.ylabel("transformada")
plt.show()

#Realicemos un calculo mas complejo con los mismos valores de N, t y f!
y_t=y_t*0
for i in range(10):
    fi=np.random.rand()*N
    amp=10#np.random.rand()*10
    y_t+=amp*np.sin(2*np.pi*fi*t)
    print(fi,amp)

y_f=fft(y_t)/N
figure=plt.subplot(211)
plt.plot(t,y_t)
plt.xlabel("time")
plt.ylabel("Signal")

figure=plt.subplot(212)

plt.plot(f[:N//2],np.abs(y_f[:N//2]))
plt.xlabel("frecuencias")
plt.ylabel("transformada")
plt.show()
