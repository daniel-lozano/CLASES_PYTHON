#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
// https://www.tutorialspoint.com/cplusplus/cpp_strings.htm

int glob;

#define PI 3.14159


double f1(double x,double y, double yp, double k);
double f2(double x,double y, double yp, double k);


// main() is where program execution begins.
int main() {
    
    int N=10000;
    double h=2.0*PI/N;
    double x[N],y[N],yp[N];
    double y0=1;
    double yp0=0;
    double k1,k2,k3,k4,l1,l2,l3,l4;
    double k=1.0;
    int i;

    for(i=0;i<N;i++)x[i]=h*i;
    
    y[0]=y0;
    yp[0]=yp0;

    //Solucionando la ecuacion
    //f''(x)=-k^2 f(x)=-sin(x)
    for(i=0;i<N-1;i++){
        
        k1=h*f1(x[i],y[i],yp[i],k);
	l1=h*f2(x[i],y[i],yp[i],k);
	
        k2=h*f1(x[i]+0.5*h,y[i]+k1*0.5,yp[i]+l1*0.5,k);
	l2=h*f2(x[i]+0.5*h,y[i]+k1*0.5,yp[i]+l1*0.5,k);
	

        k3=h*f1(x[i]+0.5*h,y[i]+k2*0.5,yp[i]+l2*0.5,k);
        l3=h*f2(x[i]+0.5*h,y[i]+k2*0.5,yp[i]+l2*0.5,k);

        k4=h*f1(x[i]+h,y[i]+k3,yp[i]+l3,k);
        l4=h*f2(x[i]+h,y[i]+k3,yp[i]+l3,k);
	

        y[i+1]=(1.0/6)*(k1+2*k2+2*k3+k4)+y[i];
	yp[i+1]=(1.0/6)*(l1+2*l2+2*l3+l4)+yp[i];

	cout << "y last " << y[i+1] << endl;
	cout << "yp last " << yp[i+1] << endl;
	
        
        
    }
    //imprimiendo en un archivo de salida
    
    ofstream file;
    file.open("solution.txt");
    file << "x " << "y "<< "y1" << endl;
    for(i=0;i<N;i++){
    	file << x[i] <<" " << y[i] << " "<< yp[i]<< endl;
    
    }
    
    
    file.close();
    
    return 0;
}

double f1(double x,double y, double yp, double k){
	return yp;
	}
double f2(double x,double y, double yp, double k){
	return -pow(k,2)*y;
	}



