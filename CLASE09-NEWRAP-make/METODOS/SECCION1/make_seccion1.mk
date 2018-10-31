#Para correr este make file se debe ejecutar el siguiente codigo
# 		make -f make_seccion1.mk
#Para hacer clean se agrega el comando al final de la linea
# Muestra la imagen de puntos Aleatorios
.PHONY: abre

abre: Aleatorios.png
	open $^

#Dependencia de los datos a plotear y el programa
Aleatorios.png: plotea.py output.txt 
	python $< output

output.txt: random.out 
	./$^

random.out: datos.cpp
	g++ -o $@ $<

clean:
	rm *.png
	rm *.txt
	rm *.out	



