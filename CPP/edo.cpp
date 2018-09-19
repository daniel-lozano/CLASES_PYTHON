#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
// https://www.tutorialspoint.com/cplusplus/cpp_strings.htm

int glob;

#define PI 3.14159

int factorial(int a);
void dont_modify( double a);
void modify1( double *a);
void modify2( double &a);
void sine_func( double x[], double f[], int N);

// main() is where program execution begins.
int main() {
    
    int N=10000;
    double h=2.0*PI/N;
    double x[N],y[N],y1[N];
    double y0=1;
    double k1,k2,k3,k4;
    int i;
    for(i=0;i<N;i++)x[i]=h*i;
    
    y[0]=y0;
    y1[0]=y0;
    //Solucionando la ecuacion
    //f'(x)=f(x)=-sin(x)
    for(i=1;i<N;i++){
        y[i]=y[i-1]-h*sin(x[i]);
        
        k1=-h*sin(x[i]);
        k2=-h*sin(x[i]+h/2);
        k3=-h*sin(x[i]+h/2);
        k4=-h*sin(x[i]+h);
        y1[i]=(1.0/6)*(k1+2*k2+2*k3+k4)+y1[i-1];
        
        
    }
    //imprimiendo en un archivo de salida
    
    ofstream file;
    file.open("solution.txt");
    file << "x " << "y "<< "y1" << endl;
    for(i=0;i<N;i++){
    file << x[i] <<" " << y[i] << " "<< y1[i]<< endl;
    
    }
    
    
    file.close();
    
    return 0;
}


