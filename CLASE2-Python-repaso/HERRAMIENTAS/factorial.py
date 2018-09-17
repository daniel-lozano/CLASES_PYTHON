#Realice un script en python el cual calcule la funcion factorial y la suma de todos los numeros enteros menores al numero que entra. Recuerde que su script debe dar un mensaje de error si el numero dado es negativo o si el numero no es entero. Recuerde que debe agregar comentarios a todo su script.

from sys import argv

numero=float(argv[1])

#primer parte----------------------------------------------------------

print numero #este es el numero que se usara para las operaciones
i=1 	     #se define la variable i
factorial=1  #aqui se guardara el resutlado del factorial
suma=0 	     #aqui se guardara el resutlado de la suma

if(numero<0):#primer mensaje de error
	print("ERROR: el numero debe ser positivo")

elif(int(numero)-numero!=0):#segundo mensaje de error
	print("ERROR: el numero debe ser un entero positivo")

else:
	print("Comenzando calculo")
	while(i<numero+1):
		factorial=factorial*i
		suma+=i
		i=i+1
		 
	print numero,"!=", factorial 
	print "la suma de todos los enteros hasta ", numero, " es", suma
	

#segunda parte----------------------------------------------------------

#tome dos numeros cualquieras y determine cual es el mayor. Luego halle el resutlado de la division. En el caso que la division sea exacta, el script debe arrojar un mensaje diciendo "la division fue exacta", en el caso contrario el programa debe dar el resutlado de la division entera y el residuo que hay. Los dos numeros deben ser enteros, por lo tanto, en el caso de que alguno no lo sea el programa debe dar un mensaje de error.

a=float(argv[2])
b=float(argv[3])

if(a<0 or b<0):#primer mensaje de error
	print("ERROR: los numeros deben ser positivo")

elif(int(a)-a!=0 or int(b)-b!=0  ):#segundo mensaje de error
	print("ERROR: el numero debe ser un entero positivo")

else:
	mayor=a
	menor=b
	if(a<b):
		mayor=b
		menor=a
	if(int(mayor/menor)- mayor/menor!=0):
		residuo=mayor -menor*(int(mayor/menor))
		print "existe un residuo!"
		print mayor, "/", menor,"=", int(mayor/menor), "con residuo ", residuo
	else:
		print "la division fue exacta!"
		print mayor, "/", menor,"=", int(mayor/menor)



