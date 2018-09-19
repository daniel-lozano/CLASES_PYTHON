import matplotlib.pyplot as plt

FILE=open("solution.txt","r")
lineas=FILE.readlines()
x=[]
y=[]

for i in range(1,len(lineas)):
    
    xp=lineas[i].split()[0]
    yp=lineas[i].split()[1]
    x.append(float(xp))
    y.append(float(yp))

plt.plot(x,y)
plt.xlabel("$ x $")
plt.ylabel("$ F(x) $")
plt.show()
