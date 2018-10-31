abrir:solucion.png
	open $<
solucion.png: grafica.py funcion_inicial_final.txt
	python $^
funcion_inicial_final.txt: a.out
	./a.out
a.out: lab11PDE.cpp
	g++ lab11PDE.cpp

clean:
	rm a.out
	rm *.txt
	rm *.png
