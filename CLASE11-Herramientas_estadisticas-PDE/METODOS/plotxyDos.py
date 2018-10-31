#CARO: plot two waves
import numpy as np
import matplotlib.pyplot as plt


uno=np.loadtxt("inicial.txt")
dos=np.loadtxt("final.txt")

plt.plot(uno[:,0],uno[:,1],label='inicial')
plt.plot(dos[:,0],dos[:,1],label='final')
plt.xlabel("x")
plt.ylabel("a(x,t)")
plt.legend()
plt.savefig("grafica.png")
