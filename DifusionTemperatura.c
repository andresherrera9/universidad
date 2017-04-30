// Intento de solucion de la ecuacion de difusion de temperatura a traves de una placa 

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// iniciar el codigo 

int main(void){

// Inicializar las variables a utilizar para la resolucion 
 	
 	float T [100][100] ; // matriz de 100 "cm" X 100 "cm"
 	float Tn[100][100];
 	float nu = 10E-4;
 	int i, j;
 	int dx = 1;  
 	int dt = 1;
 	int t;
 	float r = nu*dt / (dx*dx);
 	

    FILE *t_0= fopen("t_0.txt", "w");
 	for (i=0; i<100; i++)
 	{
 		for (j=0; j<100; j++)
 		{
 		
 			if ((i >= 45) && (i <= 55) && (j >= 20) && ( j <= 40))
 			{
				T[i][j] = 100;
			}
			else
			{
				T[i][j] = 50;
			}
			
			}}
			
			 
    scanf("%f", T[i][j]);
    fprintf(t_0, "%f\n", T[i][j]); // arroja los datos de la informacion de la placa en el tiempo = 0 
    
    fclose(t_0);
	 
	 // se quiere aplicar la metodologia de diferencias finitas para pasar la informacion a traves de la "malla" para distintos tiempos
	 
	 
	 
	 FILE *t_1;
    
    t_1 = fopen("t_1.txt", "w");
	 for(dt=0;dt<100;dt++)   // equivale a 100 segundos 
	{
		for(i=0;i<100;i++)
		{
			for(j=0;j<100;j++)
			{
				Tn[i][j] = T[i][j];
			}
		}
	
		{ T[i][j]=Tn[i][j]+(r)*(Tn[i][j+1]+ Tn[i][j-1] + Tn[i-1][j] + Tn[i+1][j] - 4*Tn[i][j]);}  // metodo de diferencias finitas
}

	 scanf("%f", T[i][j]);
    fprintf(t_1, "%f\n", T[i][j]); // arroja los datos de la informacion de la placa en el tiempo = 0 
    
    fclose(t_1);

		
	FILE *t_2;
    
    t_2 = fopen("t_2.txt", "w");
	 for(dt=0;dt<250;dt++)   // equivale a 250 segundos 
	{
		for(i=0;i<100;i++)
		{
			for(j=0;j<100;j++)
			{
				Tn[i][j] = T[i][j];
			}
		}
	
		{ T[i][j]=Tn[i][j]+(r)*(Tn[i][j+1]+ Tn[i][j-1] + Tn[i-1][j] + Tn[i+1][j] - 4*Tn[i][j]);} 
}

	 scanf(" %f", T[i][j]);
    fprintf(t_2, "%f\n", T[i][j]); // arroja los datos de la informacion de la placa en el tiempo = 0 
    
    fclose(t_2);
    
 // Condiciones constantes, bordes a misma temperatura 
 
 	for (t= 0; t<1000; t++){
 		for ( i = 0; i<100; i++){
 			for (j=0;j<100; j++){
 				if ((i == 100) && (j <= 100) && (i==0) && (j<=100))  // condiciones en los bordes a temperatura constante 
 				{
				T[i][j] = 50;
			}
				else
			{
				Tn[i][j] = T[i][j];
			
			}}}}
		    }
	 
	 
	 	 
	 
	 
	 
	 
	 
	 
	 
	 
