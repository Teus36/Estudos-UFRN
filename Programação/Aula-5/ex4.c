#include <stdio.h>

int main(){
   int n = 0;
   int fatorial;

   printf("Digite um valor para N: ");
   scanf("%d", &n);

   for(int i = n; i >= 1 ; i--) {
	fatorial *= i;
   }

   printf("%d", fatorial);

   return 0;
}
