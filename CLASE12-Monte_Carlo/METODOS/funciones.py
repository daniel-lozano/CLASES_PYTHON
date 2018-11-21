import numpy as np
import matplotlib.pyplot as plt

def F1(x,y,yp):
    return yp

def F2(x,y,yp,b,c):
    return (-b*x*yp-c*y)/(2*x**2)

def Soluciona(x,y,yp,dx,b,c):

    for i in range(1,len(y)):
        y[i]=y[i-1]+F1(x[i-1],y[i-1],yp[i-1])*dx
        yp[i]=yp[i-1]+F2(x[i-1],y[i-1],yp[i-1],b,c)*dx
    return y



#y,yp=Soluciona(x,y,yp,dx)
#print y
#plt.scatter(x,-(2./11)*x**(-3)+(2./11)*x**(5./2),s=5)
#plt.plot(x,y,"k")
#plt.show()
