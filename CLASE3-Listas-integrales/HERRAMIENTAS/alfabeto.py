infile=open("the_quixote_c3.txt","r")#se lee el archivo del quijote
output=open("dictionary.txt","w")

lineas=infile.readlines()#se separa en un arreglo que contiene las lineas del quijote 

full_text=[]#se crea un arreglo que contendra todo el texto

for line in lineas:    
    full_text.extend(line.split())#se agrega el texto...

dictionary=tuple(set(full_text))#se crea el diccionario de palabras

probability=[]

number_of_words=float(len(full_text))
print number_of_words
print len(dictionary)
suma=0

for i in dictionary:
    suma=suma+full_text.count(i)/number_of_words
    probability.append((i,full_text.count(i)/number_of_words))
    output.write(i+" "+str(full_text.count(i)/number_of_words)+"\n")
    
print suma

