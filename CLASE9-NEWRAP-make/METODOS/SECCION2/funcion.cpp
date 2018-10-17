#include <iostream>
#include <cmath>
#include <cstdlib>
#include <fstream> 
#include <ctime>
#include <string>
#include <sstream>
using namespace std;

int main(){
	ifstream inFile;
	ofstream outFile; 
	inFile.open("output.txt");
	outFile.open("sin.txt");
	int i,j;
	int N=0;
	char output[100];

	//Encuentra el numero de lineas de un archivo
	string aLineStr;
	while (getline(inFile, aLineStr)){
	    if (!aLineStr.empty())N++;
		
	}
	inFile.close();
	inFile.open("output.txt");	
	cout << "Numero de lineas=" << N << endl;

	//filling x

	float X[N],F[N];
	i=0;	
	if (inFile.is_open()) {
 		while (!inFile.eof()) {
   			inFile >> output;
			X[i]=atof(output);
			F[i]=sin(X[i]);
   			outFile <<  X[i] << " " <<  F[i] << endl;
			i++;
		}
	}
	inFile.close();
	outFile.close();

	
	
	


return 0;
}
