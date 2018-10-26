import numpy as np
import matplotlib.pyplot as plt
from sys import argv

name=argv[1]
FILE=np.loadtxt(name)
x=np.array(FILE[:,0])
y1=np.array(FILE[:,1])
y2=np.array(FILE[:,2])
y_teo=x*np.sin(x)

plt.plot(x,y_teo,"k",label="teo")
plt.plot(x,y1,"b-",label="RK")
plt.plot(x,y2,"r--",label="Euler")
plt.xlabel("x")
plt.legend()
plt.show()
plt.close()

plt.subplot(111)
plt.title("Error")
plt.plot(x,abs(y_teo-y1),"k",label="RK")
plt.plot(x,abs(y_teo-y2),"r",label="EU")
plt.xlabel("x")
plt.legend()
plt.show()
