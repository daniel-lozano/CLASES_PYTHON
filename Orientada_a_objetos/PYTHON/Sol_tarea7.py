import numpy as np
import matplotlib.pyplot as plt

#---------Definiendo dominio y funcion de x-------------------------------------

x=np.linspace(0,2*np.pi,1000)#Crea un arreglo de longitud 1000 de 0 a 2\pi

f=np.sin(x)#crea la funcion seno


plt.plot(x,f, label="$ \sin(x)   $")
plt.legend()
plt.xlabel("$ x $",size=18)
plt.ylabel("$ f(x) $",size=18)
plt.grid()
plt.show()
plt.close()

#---------Hallando maximo de la funcion y posicion del maximo-------------------

max_f=max(f)# Halla el valor maximo del arreglo f

index=np.where(f==max_f) #Halla el indice donde la funcion encuentra su maximo

print "index=",index # Da las posiciones donde la funcion llega a su maximo

print "en las posiciones ",x[index],"Se llega a los valores maximos ",f[index]


#---------Hallando derivada en el punto maximo----------------------------------

derivative_at_max= (f[index[0]]-f[index[0]-1])/(x[index[0]]-x[index[0]-1])
print "Back point f'(x_max)=",derivative_at_max

derivative_at_max= (f[index[0]+1]-f[index[0]])/(x[index[0]+1]-x[index[0]])
print "Advanced point f'(x_max)=",derivative_at_max

#-------------------Calculando derivadas---------------------------------------

g=(f[1:]-f[:999])/(x[1:]-x[:999])
plt.plot(x[1:],g,label="$  \\frac{df}{dx}   $")
plt.xlabel("$ x $",size=18)
plt.ylabel("$ g(x) $",size=18)
plt.legend()
plt.grid()
plt.show()
plt.close()

h=np.diff(f)/np.diff(x)
plt.plot(x[1:],h,label="$  \\frac{df}{dx}   $")
plt.xlabel("$ x $",size=18)
plt.ylabel("$ g(x) $",size=18)
plt.title("usando np.diff")
plt.legend()
plt.grid()
plt.show()
plt.close()




#---------------Calculo del valor absoluto-------------------------------------

cos=np.cos(x[1:])
dif=abs(cos-g)
print "maxima diferencia= ",max(dif)

plt.plot(x[1:],dif,label="$ | f^\\prime -\cos(x)    |  $")
plt.xlabel("$ x $",size=18)
plt.legend()
plt.grid()
plt.show()

#-------------Statistics of the array--------------------------------------------

mean=g.mean()
average=np.average(g)
median=np.median(g)


print "mean=",mean
print "average=",average
print "median=",median



