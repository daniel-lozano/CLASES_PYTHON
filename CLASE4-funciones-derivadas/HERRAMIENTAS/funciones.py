def primos(N):#Funcion que halla una lista de numeros primos 
    P=[2]
    for i in range(3,N+1):
        primo=0
        for j in range(len(P)):
            if(i//P[j]==1.0*i/P[j]):
                primo=1
                break

        if(primo==0):
            P.append(i)
    return P


def decomp(N,P):#funcion que da la descomposicion prima de un numero
    division=float(N)
    dec=[]
    
    i=0
    while i<len(P):
        if(division/P[i]==division//P[i]):
            division=division/P[i]
            dec.append(P[i])
            i=i-1
        i=i+1
    return dec

def mcd(D1,D2):#halla el maximo comun divisior
    mcd=1
    hallo=0
  
    for i in range(len(D1)):
        
        if(D2.count(D1[i])>0 and hallo==0):
            mcd=mcd*D1[i]
            hallo=1
    
    return mcd


def Mcd(D1,D2):#halla el maximo comun divisior
    mcd=1
    anterior=0
    counter=1
    
    for i in range(len(D1)):
        
        if(D2.count(D1[i])>=counter):
            mcd=mcd*D1[i]
            counter+=1
        if(i!=len(D1)-1 and D1[i]!=D1[i+1]): #reinicia el contador
            counter=1
        
        anterior=D1[i]
    return mcd
    
			
		
