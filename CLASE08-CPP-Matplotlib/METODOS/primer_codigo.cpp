#include <iostream> //Basico para imprimir
#include <cmath>  //Funciones matematicas tipicas
#include <cstdlib> //Para numeros random
#include <ctime> //Para tomar el tiempo actual
#include <fstream> // Para trabajar con archivos
using namespace std;
// https://www.tutorialspoint.com/cplusplus/cpp_strings.htm


//Defina una variable global llamada PI
#define PI 3.14159

double Area(double r);
int factorial(int a);
void Area_y_Perimetro(double r, double &Area, double &perimetro);
double dot_product(double V1[],double V2[],int N);
void suma_vectores(double V1[],double V2[],double V3[],int size);
void print_matriz(int N1, int N2, double** M);


// main() is where program execution begins.
int main() {
    
    //Mirando numeros random con srand
    int i,j,k,num,radio;
    int dot=0;
    int N;
    double Area,perimetro;

    cout << "Numero de valores al azar, N=" <<":";
    cin >> N;
    srand(time(NULL));
    
    
    cout << "------------------Primer Punto------------------"<< endl;

    cout << "Hello World" << endl; // prints Hello World with an enter
    cout << "Mirando numeros random" << endl;
    
    for(i=0;i<N;i++){
        radio=rand()%5;
        Area_y_Perimetro(radio, Area,perimetro);
        cout << "Radio= "<< radio << " Area=" << Area << " Perimetro="<< perimetro<<endl; // prints Hello World with an enter
        
    }
    cout << "------------------Segundo Punto------------------"<< endl;
    
    // Producto Punto de dos vectores
    double* V1=NULL;
    double* V2=NULL;
    double* V3=NULL;
    int size;
    cout << "Dimension de los vectores="<< ":";
    cin >> size;
    
    V1= new double[size];
    V2= new double[size];
    V3= new double[size];

    ofstream file;
    file.open("vectores.txt");
    
    cout << "Llenando los vectores" << endl;
    
    file << "V1 "<< "V2 "<< "V3"<< endl;

    for(i=0;i<size;i++){
        
        num=rand()%5;
        dot+=num;
        
        V1[i]=1;
        V2[i]=num;
        
    }
    
    cout << "Producto punto= "<< dot_product(V1,V2,size)<<endl;
    cout << "Producto punto= "<< dot<<endl;
    
    
    
    suma_vectores(V1,V2,V3,size);
    for(i=0;i<size;i++){
        
        file << V1[i]<<" "<< V2[i]<< " "<< V3[i]<< endl;
        
    }
    
    file.close();

    cout << "------------------Tercer Punto------------------"<< endl;
    //Iniciando las matrices
    double** M1=new double*[size];
    double** M2=new double*[size];
    double** RES=new double*[size];
    
    for(i=0;i<size;i++){
        M1[i]=new double[size];
        M2[i]=new double[size];
        RES[i]=new double[size];
        }

    cout << "Matriz M2"<< endl;
    for(i=0;i<size;i++){
        for(j=0;j<size;j++){
           
            
            if(i==j)M1[i][j]=1;
            else M1[i][j]=0;
            
            M2[i][j]=rand()%10;
            
            RES[i][j]=0;
        }
    }
    cout << "Matriz M1"<< endl;
    print_matriz(size,size,M1);
    
    cout << "Matriz M2"<< endl;
    print_matriz(size,size,M2);
    
    cout << "Matriz RES"<< endl;
    print_matriz(size,size,RES);

    
    
    cout << "Resultado"<< endl;
    for(i=0;i<size;i++){
        for(j=0;j<size;j++){
            for(k=0;k<size;k++){
                RES[i][j]+=M1[i][k]*M2[k][j];
            }
        }
    }
    cout << "Matriz RES"<< endl;
    print_matriz(size,size,RES);
    

   
    return 0;
    
    
    
}

double Area(double r){
    return PI*pow(r,2);
    }

void Area_y_Perimetro(double r, double &Area, double &perimetro){
    Area=PI*pow(r,2);
    perimetro=2*PI*r;
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

double dot_product(double V1[],double V2[],int N){
    double suma=0;
    int i;
    for(i=0;i<N;i++){
        suma+=V1[i]*V2[i];
    }
    return suma;
}
void suma_vectores(double V1[],double V2[],double V3[],int size){
    int i;
    for(i=0;i<size;i++){
        V3[i]=V1[i]+V2[i];
    }
}
void print_matriz(int N1, int N2, double** M){
    int i,j;
    for(i=0;i<N1;i++){
        for(j=0;j<N2;j++){
            cout<<M[i][j]<<" ";
        }
        cout << endl;
    }
}



