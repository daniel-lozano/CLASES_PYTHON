import numpy as np
import matplotlib.pyplot as plt
from sys import argv

name=argv[1]
FILE=np.loadtxt(name)
x=FILE[:,0]
y=FILE[:,1]
 
plt.plot(x,y,"o-")
plt.xlabel("# Pasos")
plt.title("Numeros aleatorios")
plt.savefig("sin.png")

