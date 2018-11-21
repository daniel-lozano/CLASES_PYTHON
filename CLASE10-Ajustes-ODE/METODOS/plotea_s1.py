import numpy as np
import matplotlib.pyplot as plt
from sys import argv

name=argv[1]
FILE=np.loadtxt(name)
x=np.array(FILE[:,0])
y1=np.array(FILE[:,1])
y2=np.array(FILE[:,2])
yt=y1**2+y2**2

plt.plot(x,y1,"b-",label="solution")
plt.plot(x,y2,"r--",label="derivative")
plt.xlabel("t")
plt.grid()
plt.legend()
plt.show()
plt.close()
plt.plot(x,yt,label="Energy")
plt.xlabel("$t\ \mathrm{Time}$")
plt.show()

