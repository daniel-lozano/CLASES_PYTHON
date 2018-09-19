#Paquetes Basicos------------------------------
import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt

#Para el manejo de algebra lineal---------------
from numpy.linalg import *
from scipy.linalg import expm,inv

#Para los plots 3D -----------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N=1000

x=uniform(0,9,N)
ruido=uniform(-2,2,N)#+np.sin(x1)
y=x+ruido*np.exp(-0.1*(x-5)**2)
z=x+y+uniform(-3,3,N)*np.exp(0.05*(-(x-np.mean(x))**2-(y-np.mean(y))**2))



