#include <iostream>
#include <cmath>
#include <cstdlib>
#include <fstream> 
#include <ctime>
using namespace std;

int main(){
	//Aqui debe generar un archivo para escribir en el
	ofstream File; 
	File.open("output.txt");
	//------------------------------------------
	int N,i;
	cout<< "De un valor de N"<< endl;
	cin >> N;
	srand(time(0));
	//Aqui debe imprimir en el archivo los datos random
	for(i=0; i<N;i++){ 
	File << i << " " << rand()%10<< endl;	
	}
	//Aqui debe cerrar el archivo
	File.close();

return 0;
}
