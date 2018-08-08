import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft,fftfreq,irfft


N=1000
t=np.linspace(0,1,N)
T=t[1]-t[0]
f1=10
f2=15

y_t_o=np.sin((f1+f2)*np.pi*t)+np.sin((f2-f1)*np.pi*t)#np.zeros(N)
for i in range(5):
    freq=20*np.random.rand()
    y_t_o +=np.sin(freq*2*np.pi*t)

y_t=y_t_o+(1-2*np.random.rand(N))

freq=np.linspace(0,1/T,N)
y_f=fft(y_t)



y_f_pow=np.abs(y_f)/N

figure=plt.subplot(211)
plt.plot(t,y_t)
plt.grid()

figure=plt.subplot(212)
plt.plot(freq[:N//2],y_f_pow[:N//2])
plt.grid()

plt.show()

#Reconstrullamos la senal a partir de las frecuencias menores a 2.5

rec_f=np.zeros(N,"complex")

for i in range(N):
    if(freq[i]<40):
        rec_f[i]=y_f[i]

Norm=np.sum(abs(rec_f))/(N*np.pi)   #   CHECK!!!!
y_rec=(ifft(rec_f))*Norm#*np.sum(np.abs(ifft(rec_f)))/N
rec_pow=np.abs(rec_f)/N

plt.subplot(311)
plt.plot(freq[:N//2],y_f_pow[:N//2])
plt.plot(freq[:N//2],rec_pow[:N//2])
plt.grid()


plt.subplot(312)
plt.plot(t,y_t,label="Original",linewidth=2.5)
plt.plot(t,y_rec.real,label="Reconstruccion")
plt.grid()
plt.legend()

plt.subplot(313)
plt.plot(t,y_t_o,label="Original no noise",linewidth=2.5)
plt.plot(t,y_rec.real,label="Reconstruccion")
plt.grid()
plt.legend()
plt.show()


plt.show()
