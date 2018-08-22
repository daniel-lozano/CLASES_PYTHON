##!/bin/bash


#chmod <opciones> <nombre del archivo>
#chmod u+wrx <nombre del archivo>
# u= usuario
# w= writing
# r=reading
# x= execution 

#punto 1
wget https://raw.githubusercontent.com/daniel-lozano/CLASES_PYTHON/master/CLASE1/HERRAMIENTAS/notas.txt
awk '{print $1,$2,$3,$6;}' notas.txt | grep  4. | awk '{if ($4>15) print $1,$2,$3,$4}' > RES1.txt

#punto 2
grep -w 0 notas.txt | awk '{if($7<6) print $1,$2}' 


#punto 3
awk '{if($7>8) print $1,$2,$3,$4,$5,$6,$7}' notas.txt > RES2.txt
wc -l RES2.txt

#punto 4
mkdir RESULTADOS
mv RES1.txt RESULTADOS
mv RES2.txt RESULTADOS



