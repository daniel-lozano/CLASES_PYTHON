import matplotlib.pyplot as plt
import numpy as np

#Primera parte: Graficar la siguiente funcion para diferentes tipos de colores y lineas dependiendo un parametro de frecuencia, para los plots se deben usar los colores rojo para f=1, azul para f=2 y verde para f=3. Utilice el parametro loc para que la leyenda aparezca en la esquina inferior derecha.

f=[1,2,3]
color=["r","b","g"]
x=np.linspace(-10,10,200)

for i in range(len(f)):
    y1=np.sin(f[i]*x)/x
    plt.plot(x,y1,color[i],label="$ \\frac{\sin(fx)}{x},\ f= $"+str(f[i]))

plt.legend(loc=4)
plt.show()

for i in range(len(f)):
    y2=np.cos(f[i]*x)*np.exp(-0.5*abs(x))
    plt.plot(x,y2,color[i],label="$ \cos(fx)e^{-|x|},\ f=$"+str(f[i]))

plt.legend(loc=4)
plt.show()


#Modificacion de graficas: Se desea que las funciones solo se grafiquen en la parte positiva. Use la funcion where para graficar su funcion a trozos tomando solo la parte positiva.
index1=np.where(y1<0)
indexpos=np.where(y2>0.3)
indexneg=np.where(y2<-0.3)
y1[index1]=0

y2[indexpos]=0.5
y2[indexneg]=-0.5
plt.plot(x,y1,label="positive")
plt.show()
plt.plot(x,y2,label="smaller than 0.5")
plt.show()





#Caminata aleatoria
alcance=[]
N=1000
file=open("caminata.txt","w")

for i in range(N):
    sumax=0
    sumay=0
    for j in range(100):
        sumax+=np.random.uniform(-1,1)
        sumay+=np.random.uniform(-1,1)
    file.write(str(round(sumax,4))+" "+str(round(sumay,4))+"\n")

    alcance.append([sumax,sumay])
file.close()

caminata=np.array(alcance)
X=caminata[:,0]
Y=caminata[:,1]
plt.hist(X,bins=20)
plt.title("Caminata en x")
plt.show()

plt.hist(Y,bins=20)
plt.title("Caminata en y")
plt.show()

R=np.sqrt(X**2+Y**2)
INDEX1=np.where(R<10)
INDEX2=np.where(R>5)

data=R[INDEX1]
print("len(R)",len(R))
print("len(data)",len(data))
X=X[INDEX2]
Y=Y[INDEX2]
print("len(X)",len(X))
print("len(Y)",len(Y))
plt.hist(R,bins=20)
plt.hist(data,bins=20)
plt.title("Caminata en r")
plt.show()

plt.scatter(X,Y)
plt.title("scatter")
plt.show()

datos=np.loadtxt("caminata.txt")
print(datos.shape)

