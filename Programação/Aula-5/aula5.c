#include <stdio.h>

int main(){
   int a, b;
   printf("Digite os valores inteiros: ");
   scanf("%d %d", &a, &b);

   while (a < b) {
        a++
	printf("%d\n", a);
   }

   printf("Fim do programa\n");

   return 0;
}