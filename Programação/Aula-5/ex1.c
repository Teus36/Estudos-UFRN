#include <stdio.h>

int main(){
   double n;

   double x = 1;
   double xnovo;
   double erro = 1;

   printf("Digite um numero para calcular a aproximacao da sua raiz quadrada: ");
   scanf("%lf", &n);

   while (erro > 0.0001) {
	xnovo = 0.5 * (x + n/x);

	erro = x - xnovo;
	
	if (erro < 0) {
	   erro = erro * (-1);
	}

	x = xnovo;
   }

   printf("A aproximacao de N: %lf", xnovo);

   return 0;
}