#include <stdio.h>

int main(){
   int n;
   int soma = 0;

   printf("Digite o valor de N: ");
   scanf("%d", &n);

   for (int i = 0; i < n; i+=2){
	soma += i;
   }

   printf("%d", soma);
   return 0; 
}