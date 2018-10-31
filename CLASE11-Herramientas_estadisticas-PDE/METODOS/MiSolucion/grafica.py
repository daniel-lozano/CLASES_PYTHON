import numpy as np
import matplotlib.pyplot as plt
from sys import argv
name=argv[1]
datos=np.loadtxt(name)
#plt.subplot(121)
plt.plot(datos[:,0],datos[:,1],label="condicion inicial")
#plt.subplot(122)
plt.plot(datos[:,0],datos[:,2],label="funcion evolucionada")
plt.legend()
plt.savefig("solucion.png")
plt.show()
