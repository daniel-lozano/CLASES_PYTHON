from sys import argv
import funciones

N1=int(argv[1])
N2=int(argv[2])
N=max([N1,N2])

#Hallar los numeros primos hasta el numero N
P=funciones.primos(N)
D1=funciones.decomp(N1,P)
D2=funciones.decomp(N2,P)

print(P)
print(N1,D1)
print(N2,D2)
#Realiza la descomposicion prima de un numero


mcd=funciones.mcd(D1,D2)
print(mcd)

MCD=funciones.Mcd(D1,D2)
print(MCD)


