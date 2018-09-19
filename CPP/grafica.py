import matplotlib.pyplot as plt

FILE=open("solution.txt","r")
lineas=FILE.readlines()
x=[]
y=[]
y1=[]

for i in range(1,len(lineas)):
    
    xp=lineas[i].split()[0]
    yp=lineas[i].split()[1]
    yp1=lineas[i].split()[2]
    x.append(float(xp))
    y.append(float(yp))
    y1.append(float(yp1))

plt.plot(x,y)
plt.plot(x,y1,"--")
plt.xlabel("$ x $")
plt.ylabel("$ F(x) $")
plt.show()
