// programa para resolver la ecuacion de advencion
// usando el esquema FTCS : forward time centered space

#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm> // std::min_element, std::max_element
using namespace std;


//impresion de archivo sin normalizar
int myarrpr(float xx[],float aaa[],int tam,char filename[])
{
  int mcount=0;
  std::cout <<std::endl;
  ofstream fp(filename);
  for(mcount=0;mcount<tam;mcount++)
        fp<<xx[mcount]<<" "<<aaa[mcount]<<endl;
     return 0;
}

//impresion de archivo normalizada
int myarrprnorm(float xx[],float aaa[],int tam,char filename[])
{
  int mcount=0;
  float maxval=*std::max_element(aaa,aaa+tam);
  std::cout <<std::endl;
  ofstream fp(filename);
  for(mcount=0;mcount<tam;mcount++)
    fp<<xx[mcount]<<" "<<aaa[mcount]/maxval<<endl;
    
  return 0;
}

#define pi 3.1416  
#define ene 50       //number of grid points


int main ()
{
float tau=0.002;  //paso en el tiempo
float ele=1.0;    //system size - dimension
float ache=ele/ene; // grid spacing
float velo=1; // velocidad del flujo


// Condicion inicial, pulso Gaussian-cosine
float sigma=0.1; // ancho del pulso gausiano
float kwave=pi/sigma;  //numero de onda del coseno


float equis[ene];
float aaa[ene];
float anew[ene];
float equisnew[ene];
float afin[ene];
float equisfin[ene];


float aux1=0;
int tam=ene;
float coeff=-velo*tau/(2*ache); // coeficiente para el metodo FTCS
cout<< "coeff="<<coeff<<endl;
int i=0;
int mcount=0;
for(mcount=0;mcount<ene;mcount++)
  {
    equis[mcount]=(mcount-0.5)*ache-(ele/2);
    aux1=equis[mcount]*equis[mcount];
    aaa[mcount]=cos(kwave*equis[mcount])*exp(-aux1/(2*sigma*sigma));

    //variables extra
    anew[mcount]=aaa[mcount];
    equisnew[mcount]=equis[mcount];
    afin[mcount]=aaa[mcount];
    equisfin[mcount]=equis[mcount];   
   }

 
 
// ciclo principal

 int nstep=int(ele/(velo*tau))+1;
 
 std::cout <<"el numero de pasos en el tiempo es "<<nstep<<std::endl;
 std::cout <<"el numero de pasos en el espacio es "<<ene<<std::endl;

  for(mcount=0;mcount<nstep;mcount++)
    {
      coeff=-velo*tau/(2*ache); // coeficiente para el metodo FTCS
          //frontera periodica
      afin[0]=anew[0]+(coeff*(anew[1]-anew[ene]));

      equisfin[0]=(velo*tau)+equisnew[0];
      
      for(i=1;i<ene;i++)
	{
	  afin[i]=anew[i]+(coeff*(anew[i+1]-anew[i-1]));
	  equisfin[i]=(velo*tau)+equisnew[i];
	}
     
    //frontera periodica
      afin[ene]=anew[ene]+(coeff*(anew[0]-anew[ene-1]));
      equisfin[ene]=(velo*tau)+equis[ene];

      
      //haciendo que equis sea periodica
      for(int ke=0;ke<ene;ke++)
	if(equisfin[ke]>0.5*ele)
	  equisfin[ke]-=ele;

      //escribiendo avance
         for(int j=0;j<ene;j++)
	   {
	     anew[j]=afin[j];
	     equisnew[j]=equisfin[j];
	   }

   }


  char name[20]="inicial.txt";
 mcount=myarrpr(equis,aaa,tam,name);
 char namedos[30]="inicialnorm.txt";
 mcount=myarrprnorm(equis,aaa,tam,namedos);
 char namefin[20]="final.txt";
 mcount=myarrpr(equisfin,afin,tam,namefin);
 char namefinnorm[20]="finalnorm.txt";
 mcount=myarrprnorm(equisfin,afin,tam,namefinnorm);

}
