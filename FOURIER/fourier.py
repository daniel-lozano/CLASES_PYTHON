#! /bin/python2.7.1

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft,fftfreq

#Datos de numero de puntos, frecuencias, tiempo, espacio entre puntos y funcion temporal

N=1000
f1=40
f2=90
t=np.linspace(0,0.5,N)
dt=t[1]-t[0]
y_t=np.sin(f1*2*np.pi*t)+ 0.5 * np.sin(f2*2*np.pi*t)

plt.plot(t,y_t)
plt.title("Grafica en tiempo")
plt.show()
'''
-------------------- Punto 1: practica de fft  --------------------------------------
'''
# A partir de la ecuacion hallada se debe hallar la transformada de la funcion y_t recordando que se debe normalizar por el factor N

Norm=1.0/N
y_f=fft(y_t)*Norm #Se realiza la transformada de fourier normalizada por N
freq = fftfreq(N, dt) #Da el rango de frecuencias que seran usadas

plt.plot(freq,abs(y_f))
plt.xlim(-100,100)
plt.title("Grafica en frecuencias")
plt.show()


'''
-------------------- Punto 2 (seccion 1): obtencion de senalaes --------------------------------------
'''

y_t=y_t*0
F_MAX=40

#Frecuancias y amplitudes a encontrar en el taller

plt.subplot(211)
frequencies=[5,20,30]
amplitudes=[27,53,82]

for i in range(len(frequencies)):
    fi=frequencies[i]#np.random.uniform(0,F_MAX)
    amp=amplitudes[i]#np.random.uniform(0,10)
    y_s=amp*np.sin(2*np.pi*fi*t)
    y_t+=y_s
    #plt.plot(t,y_s,label="$ f =$"+str(fi)+", $\\mathrm{Amp}=$"+str(amp))
    print(fi,amp)

y_f=fft(y_t)/N# Se realiza la transformada de Fourier

#Escribe el archivo de datos que sera compartido
file=open("datos_s1.txt","w")
file.write("t y_t\n")
for i in range(len(y_f)):
    file.write(str(t[i])+" "+str(y_t[i])+"\n")
file.close()

plt.plot(t,y_t,label="suma")
plt.xlabel("time")
plt.ylabel("Signal")
plt.legend()
plt.subplot(212)

plt.plot(freq[:N//2],np.abs(y_f[:N//2]))
plt.xlim(0,2*F_MAX)
plt.xlabel("frecuencias")
plt.ylabel("transformada")
plt.show()

#Se buscan las frecuencias de interes y se filtra la senal tomando las frecuencias por aparte

first=y_f.copy()
first[abs(freq)>15]=0
plt.plot(freq[:N//2],np.abs(first[:N//2]))

second=y_f.copy()
second[abs(freq)>25]=0
second[abs(freq)<15]=0
plt.plot(freq[:N//2],np.abs(second[:N//2]))

third=y_f.copy()
third[abs(freq)<25]=0
plt.plot(freq[:N//2],np.abs(third[:N//2]))
plt.xlim(0,2*F_MAX)
plt.show()

#Se hallan las transformadas inversas de la senal

y1=np.real(ifft(first))
y2=np.real(ifft(second))
y3=np.real(ifft(third))
plt.plot(t,y1)
plt.plot(t,y2)
plt.plot(t,y3)
plt.show()

#Se comprueba que la senal recuperada, la suma, es igual que la senal original

plt.plot(t,N*(y1+y2+y3),"o",label="cleaned")
plt.plot(t,y_t,"--",label="reconstructed")
plt.legend()
plt.show()


'''
-------------------- Punto 2 (seccion 2): obtencion de senalaes --------------------------------------
'''

y_t=y_t*0
F_MAX=40

#Frecuancias y amplitudes a encontrar en el taller

plt.subplot(211)
frequencies=[5,20]
amplitudes=[27,53]

ruido=(np.random.rand(N)*3+2)*15
y_t+=ruido
for i in range(len(frequencies)):
    fi=frequencies[i]#np.random.uniform(0,F_MAX)
    amp=amplitudes[i]#np.random.uniform(0,10)
    y_s=amp*np.sin(2*np.pi*fi*t)
    y_t+=y_s
    #plt.plot(t,y_s,label="$ f =$"+str(fi)+", $\\mathrm{Amp}=$"+str(amp))
    print(fi,amp)

y_f=fft(y_t)/N# Se realiza la transformada de Fourier

#Escribe el archivo de datos que sera compartido
file=open("datos_s2.txt","w")
file.write("t y_t\n")
for i in range(len(y_f)):
    file.write(str(t[i])+" "+str(y_t[i])+"\n")
file.close()

plt.plot(t,y_t,label="suma")
plt.xlabel("time")
plt.ylabel("Signal")
plt.legend()
plt.subplot(212)

plt.plot(freq[:N//2],np.abs(y_f[:N//2]))
plt.xlim(0,2*F_MAX)
plt.xlabel("frecuencias")
plt.ylabel("transformada")
plt.show()

#Se buscan las frecuencias de interes y se filtra la senal tomando las frecuencias por aparte

first=y_f.copy()
first[abs(freq)>15]=0
#first[abs(freq)<1]=0
plt.plot(freq[:N//2],np.abs(first[:N//2]))

second=y_f.copy()
second[abs(freq)>25]=0
second[abs(freq)<15]=0
plt.plot(freq[:N//2],np.abs(second[:N//2]))
plt.xlim(0,2*F_MAX)
plt.show()


#Se hallan las transformadas inversas de la senal

y1=np.real(ifft(first))
y2=np.real(ifft(second))
plt.plot(t,y1)
plt.plot(t,y2)
plt.show()

#Se comprueba que la senal recuperada, la suma, es igual que la senal original


plt.plot(t,y_t,"b-",label="original")
plt.plot(t,N*(y1+y2),"r-",label="cleaned")
plt.legend()
plt.show()










