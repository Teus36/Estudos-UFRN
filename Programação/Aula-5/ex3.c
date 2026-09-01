#include <stdio.h>

int main(){
   int n;
   int a = 0, b = 1, proximo;
   int contador = 0;

   printf("Digite um valor para N:" );
   scanf("%d", &n);

   for (int i = 1; i <= n; i++) {
	printf("%d", a);

	proximo = a + b;
	b = a;
	a = proximo;
   }

   printf("A soma dos %d primeiros termos é: ", soma);

   return 0;
}


