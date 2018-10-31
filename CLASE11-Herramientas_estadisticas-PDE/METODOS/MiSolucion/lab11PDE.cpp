// programa para resolver la ecuacion de advencion
// usando el esquema FTCS : forward time centered space

#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm> // std::min_element, std::max_element
using namespace std;


#define pi 3.141592
#define ene 50       //number of grid points

float c=1; // velocidad del flujo
float sigma=0.1; // Sigma
float lambda=2*pi/sigma; // lambda
float L=2; // Longitud total del tiempo
float Time=1; // Tiempo total de evolucion
float k=pi/sigma; // Numero de onda


float initial(float x,float t,float x0);

int main ()
{
    float tau=0.001;  //paso en el tiempo
    float h=1./200.; // grid spacing

    int N=int(L/h);
    int N_t=500;//int(Time/tau);
    cout << "N="<< N<< " N_t="<<N_t<<endl;
    
    ofstream FILE;
    
    //Defining initial condition
    float x[N];
    float t[N_t];
    float func_old[N];
    float func_init[N];
    float func_new[N];
    
    //Defining space spacing
    for(int i=0; i<N;i++){
        x[i]=i*h-L/2;
    }
    //Defining time spacing
    for(int i=0; i<N_t;i++){
        t[i]=i*tau;
    }
    //iniciando programa
    
    for(int i=0;i<N;i++){
        func_init[i]=initial(x[i],t[0],0);
        func_old[i]=initial(x[i],t[0],0);
    }

    //Solucionando con condiciones periodidas
    
    int j,i;
    cout<< "Coeficiencie=" <<tau*c/h<<endl;
    for(j=1;j<N_t;j++){
        
        func_new[0] = func_old[0]-(func_old[1]-func_old[N-1])*tau*c/(2*h);
        for(i=1; i<N-1 ; i++){
            // every component but the last one
            func_new[i] = func_old[i]-(func_old[i+1]-func_old[i-1])*tau*c/(2*h);
            //func_new[i] = func_old[i]*(1+tau*c/h)-func_old[i+1];
        }
        //last point
        
        func_new[N-1]=func_old[N-1]-(func_old[0]-func_old[N-2])*tau*c/(2*h);
        
        for(i=0; i<N ; i++) func_old[i]=func_new[i];
        
    }
   
    
    
    FILE.open("funcion_inicial_final.txt");
    float maxval=*std::max_element(func_new,func_new+N);
    for(int i=0;i<N;i++){
       
        FILE<< x[i]<< " "<< func_init[i]<<" "<< func_new[i]/maxval<< endl;
    }
    FILE.close();
    
    
    return 0;
    
}

float initial(float x,float t,float x0){
    
    return cos(k*(x-(x0+c*t)))*exp(-0.5*pow(x-(x0+c*t),2)/pow(sigma,2));
}
