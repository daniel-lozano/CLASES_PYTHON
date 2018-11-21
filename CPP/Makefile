.PHONY: second_derivarite.png 
	

second_derivative.png: solution.txt
	python grafica.py

solution.txt:
	g++ -o edo.out sedo.cpp
	./edo.out

abrir: 
	open second_derivative.png

clean:
	rm *.png
	rm *.txt
	rm *.out
