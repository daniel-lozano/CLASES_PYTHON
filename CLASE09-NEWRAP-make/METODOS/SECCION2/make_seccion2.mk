#Para correr este make file se debe ejecutar el siguiente codigo
# 		make -f make_seccion2.mk
#Para hacer clean se agrega el comando al final de la linea

# Muestra la imagen de puntos Aleatorios
.PHONY: abre

abre: sin.png
	open $^

#Dependencia de los datos a plotear y el programa
sin.png: plotea.py sin.txt 
	python $< sin.txt

sin.txt: sin_x output.txt
	./$<

output.txt: datos_x
	./$^

sin_x: funcion.cpp
	g++ -o $@ $^

datos_x: datos.cpp
	g++ -o $@ $^

clean:
	
	rm *.txt
	rm *_x
	rm *.png	



