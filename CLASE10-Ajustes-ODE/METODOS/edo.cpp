#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
// https://www.tutorialspoint.com/cplusplus/cpp_strings.htm


#define PI 3.14159
double f1(double x,double y);

// main() is where program execution begins.
int main() {
    
    int N=10000;
    double h=4.0*PI/N;
    double x[N],y[N],y_e[N];
    double y0=0;
    double k1,k2,k3,k4;
    double k=1.0;
    int i;

    for(i=0;i<N;i++)x[i]=h*i;
    
    y[0]=y0;
    y_e[0]=y0;

    //Solucionando la ecuacion
    //f''(x)=-k^2 f(x)=-sin(x)
    for(i=0;i<N-1;i++){
        
        k1=h*f1(x[i],y[i]);
	
        k2=h*f1(x[i]+0.5*h,y[i]+k1*0.5);
	
        k3=h*f1(x[i]+0.5*h,y[i]+k2*0.5);

        k4=h*f1(x[i]+h,y[i]+k3);
	

        y[i+1]=(1.0/6)*(k1+2*k2+2*k3+k4)+y[i];
        y_e[i+1]=y_e[i]+h*f1(x[i],y_e[i]);

        //cout << "y last " << y[i+1]<< "y last euler" << y_e[i+1] << endl;
	
    
    }
    //imprimiendo en un archivo de salida
    
    ofstream file;
    file.open("compare.txt");
    //file << "x " << "y "<< "y_e" << endl;
    for(i=0;i<N;i++){
    	file << x[i] <<" " << y[i] << " "<< y_e[i] << endl;
    
    }
    
    
    file.close();
    
    return 0;
}

double f1(double x,double y){
	return sin(x)+x*cos(x);
	}



