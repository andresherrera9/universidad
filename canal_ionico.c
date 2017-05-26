#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<time.h>


double bet;
int i;
int a;
int b;
double xi[84];
double yi[84];
double radio(double x, double y);
int suma = 0;
double h = 0.2;


int main(void){
srand((unsigned ) time(NULL));
FILE *datosx;
FILE *datosy;
    
double x = -1.5;
double xo = 0;
double y = 8.0;
double yo = 0;
double x1 = 0;
double y1 = 0;
double dx = 0;
double dy = 0;
int test;



FILE *archivo=fopen("datos.txt","w+");   	
datosx=fopen("CanalIonico_x.txt", "r");
FILE *out=fopen("datos1.txt","w+"); 
datosy=fopen("CanalIonico_y.txt", "r");
    

i=0;
    do{
        test= fscanf(datosx,"%lf\n", &x);
        xi[i] = x;
        i = i+1;
        
    } while(test!=EOF);
    suma=84;
    
    

    
i=0;
    do{
        test= fscanf(datosy,"%lf\n", &y);
        yi[i] = y;
        
        i = i+1;
        
    } while(test!=EOF);
    suma=84;
    
    
    
   
    for(i = 0; i<200000;i++){
          fprintf(archivo, "%f %f\n", x, y);
          
          	x1 = x + h*dx;
            y1 = y + h*dy;
        
            dx= ((double)rand()/RAND_MAX)*2-1.0;
            dy= ((double)rand()/RAND_MAX)*2-1.0;
        
            
          
          double alpha = radio(x1,y1)/radio(x,y) ;
            if(alpha >1){
            x = x1;
            xo = x;
            y = y1;
            yo = y;
            
            }
            else{
			bet = (double)rand()/RAND_MAX;
                 if(bet>alpha){
					x = x1;
					y = y1;
                 }
                 }
fprintf(out,"%f %f %f\n", x1,y1, radio(x1,y1));	
                 }

printf("sol = %f %f %f\n", x1,y1, radio(x1,y1));
    
	  
		}
          
double radio(double x, double y){
       bet = 0;
       double sol = (double)RAND_MAX;
       for(b = 0;b<suma/2;b++){
             bet = sqrt( pow((x-xi[b]),2) + pow((y-yi[b]),2))-1;
             if(bet<sol){
                       sol = bet;
                       }
             }
       return sol;
       }
       
       
// Se grafico un circulo para los valores obtenidos en la terminal. Estos presentan valores muy grandes
// en las primeras dos iteraciones algunas veces. La tercera suele presentar los valores acertados para la solucion 




     






       