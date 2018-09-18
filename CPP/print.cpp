#include <iostream>
#include <cmath>
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
    glob=1.0;
    
    int a=2;
    int b=1;
    int i,j,k;
    double c=a*b*0.3;
    
    cout << "Hello World" << endl; // prints Hello World with an enter
    
    cout << glob << endl;
    cout << PI << endl;
    cout << c << endl;
    
    //loops in c++
    for(i=0;i<10;i++){
        cout << i <<"!="<< factorial(i) << endl;
    }
    
    // how NOT to  modify variables
    cout << "a before " << a << endl;
    dont_modify(a);
    cout << "a after " << a << endl;

    
    // how to  modify variables
    c=1.0;
    double d=2.0;
    cout << "c before " << c << endl;
    modify1(&c);
    cout << "c after " << c << endl;
    
    cout << "d before " << d << endl;
    modify2(d);
    cout << "d after " << d << endl;
    
    int N=1000;
    double x[N];
    double f[N];
    
    for(int i=0; i< N; i++){
        x[i]=(i+1)*2*PI/N;
        
    }
    cout << "2pi=" << x[N-1] << endl;
    sine_func(x, f,  N);
    cout << "sin(2pi)=" << f[N-1] << endl;

    
    
    return 0;
}



int factorial(int a){
    
    int res=1;
    if(a!=0){
        for(int i=1;i<a+1;i++){
            res*=i;
            
        }
    }
    return res;
}

void dont_modify( double a){
    a=a*2;
}
void modify1( double *a){
    *a = *a*2;

}
void modify2( double &a){
    a = a*2;
    
}

void sine_func( double x[],double f[], int N){

    for(int i=0; i<N; i++){
        f[i]=sin(x[i]);
    
    }
}
