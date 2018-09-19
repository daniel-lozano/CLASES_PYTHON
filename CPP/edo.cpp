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
    double h=1.0/N;
    double x[N],y[N];
    double y0=0;
    int i;
    for(i=0;i<N;i++)x[i]=h*i;
    
    y[0]=y0;
    //Solucionando la ecuacion
    
    for(i=1;i<N;i++){
        y[i]=y[i-1]+h*exp(x[i]);
    }
    //imprimiendo en un archivo de salida
    
    ofstream file;
    file.open("solution.txt");
    file << "x " << "y" << endl;
    for(i=0;i<N;i++){
    file << x[i] <<" " << y[i] <<  endl;
    
    }
    
    
    file.close();
    //f'(x)=f(x)=e^x
    return 0;
}


