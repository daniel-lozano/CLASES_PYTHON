
import numpy as np
import matplotlib.pyplot as plt

tolerance=1E-4
x=np.linspace(-7,7,1E3)

'''
   ------------------------------------------------------------------------------------------------------------------------------------
                                                                        FUNCTIONS
   ------------------------------------------------------------------------------------------------------------------------------------
'''


def func1(x):
    return (x+np.pi)*(x-np.pi)*(x-2*np.e)
def func2(x):
    return (x+np.e)*(x-np.e)*(x-2*np.pi)

true_roots1=np.array([-np.pi,np.pi,2*np.e])
true_roots2=np.array([-np.e,np.e,2*np.pi])

def fuerza_bruta(func,x):
    
    roots=[]
    for i in range(1,len(x)):
        
        if( np.sign(func(x[i-1]))!=np.sign(func(x[i])) ):
            roots.append(x[i-1])
    return np.array(roots)


def find_zero_bisection(a,b,tol,func):
    
    if( func(a)*func(b) >0 ):
        raise Exception('No single zero between the points\n')
    
    mid=(b+a)/2.0 #Define a middle point

    while (b-a)/2>tol: # While the tolerance is smaller than the difference...
    
        if(func(mid)==0): # if the zero was found
            return mid
        elif (func(mid)*func(a)<0): #if they both, a and c, differ in signs
            b=mid
        else: #
            a=mid
        mid=(b+a)/2.0

    return mid

def find_zero_bisection_pasos(a,b,tol,func):
    pasos=0
    if( func(a)*func(b) >0 ):
        raise Exception('No single zero between the points\n')
    
    mid=(b+a)/2.0 #Define a middle point
    
    while (b-a)/2>tol: # While the tolerance is smaller than the difference...
        
        if(func(mid)==0): # if the zero was found
            return mid
        elif (func(mid)*func(a)<0): #if they both, a and c, differ in signs
            b=mid
        else: #
            a=mid
        mid=(b+a)/2.0
        pasos+=1
    
    return mid,pasos



def f_prime(func,x):
    h=1E-5
    return (func(x+h)-func(x-h))/(2.0*h)

def newton_raphson(x,steps,func):
    
    for i in range(steps):
        
        if f_prime(func,x)==0:
            return x
        
        x=x-func(x)/f_prime(func,x)

    return x



'''
    ------------------------------------------------------------------------------------------------------------------------------------
                                                            STARTING PROGRAM
    ------------------------------------------------------------------------------------------------------------------------------------
'''

#Primera parte: halle una primera aproximacion de las raices usando el metodo de cambio de signo (fuerza bruta), guarde las raices halladas en un arreglo
#Halle las diferencias consecutivas del arreglo de raices que acaba de definir, de esta manera ud puede saber cual es la distancia minima que hay entre cada raiz.
print " ------------------------------------------------------------"
print "                         SECCION 1"
print " ------------------------------------------------------------\n"
roots=fuerza_bruta(func1,x)
better_roots=roots.copy()
best_roots=roots.copy()

difference=roots[1:]-roots[0:-1]

jump=min(difference)/5.0 #defined for the bisection method

for i in range(len(roots)):
    
    better_roots[i]=find_zero_bisection(roots[i]-jump,roots[i]+jump,tolerance,func1)
    best_roots[i]=newton_raphson(roots[i],5,func1)

print "fuerza bruta",roots,abs((roots-true_roots1)/true_roots1)
print "bisection ayudado", better_roots,abs((better_roots-true_roots1)/true_roots1)

print "Newton Raphson ayudado", best_roots,abs((best_roots-true_roots1)/true_roots1)

print " ------------------------------------------------------------"
print "                         SECCION 2"
print " ------------------------------------------------------------\n"

roots=fuerza_bruta(func2,x)
better_roots=roots.copy()
best_roots=roots.copy()

difference=roots[1:]-roots[0:-1]

jump=min(difference)/4.0 #defined for the bisection method

for i in range(len(roots)):
    better_roots[i]=find_zero_bisection(roots[i]-jump,roots[i]+jump,tolerance,func2)
    best_roots[i]=newton_raphson(roots[i],5,func2)

print "fuerza bruta",roots,abs((roots-true_roots2)/true_roots2)

print "bisection ayudado", better_roots,abs((better_roots-true_roots2)/true_roots2)

print "Newton Raphson ayudado", best_roots,abs((best_roots-true_roots2)/true_roots2)





#Parte 2: Halla la eovlucion del error

print " ------------------------------------------------------------"
print "                       Parte 2  SECCION 1"
print " ------------------------------------------------------------\n"

print "Halla la evolucion del error en funcion del numero de pasos del metodo Newton-Raphson"

N=np.array([1,2,3,4,5])
Error=np.zeros(len(N))
x0=5

for i in range(len(N)):
    root_found=newton_raphson(9,N[i],func1)
    Error[i]=abs((root_found-2*np.e)/(2*np.e))
plt.semilogy(N,Error)
plt.title("$\mathrm{Error\ evolution} $")
plt.xlabel("$N\ \mathrm{Iterations}$")
plt.ylabel("$\mathrm{Error}$")
plt.show()

print " ------------------------------------------------------------"
print "                       Parte 2  SECCION 2"
print " ------------------------------------------------------------\n"

print "Halla la evolucion del numero de pasos en el metodo de biseccion"

tau=np.array([1E-1,1E-2,1E-3,1E-4,1E-5])
ticks=range(0,5)
eticks=tau.astype(str)
Pasos=np.zeros(len(tau))


for i in range(len(tau)):
    Pasos[i]=find_zero_bisection_pasos(6,8,tau[i],func2)[1]
plt.plot(Pasos,"o")
plt.xticks(ticks,tau)
plt.title("$\mathrm{Step\ evolution} $")
plt.xlabel("$\mathrm{Tolerance}$")
plt.ylabel("$N\ \mathrm{Steps}$")
plt.show()








