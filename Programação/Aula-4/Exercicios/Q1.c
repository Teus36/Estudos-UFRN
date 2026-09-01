#include <stdio.h>

int main() {
    int valor1, valor2, valor3;
    
    printf("Digite 3 valores para formar um triangulo: ");
    scanf("%d %d %d", &valor1, &valor2, &valor3);
   

    // Verificação para formar um triângulo
    
    if ((valor1 && valor2 && valor3) > 0) {
       printf("Todos os lados sao positivos\n");

       if (valor1 > valor2 + valor3 || valor2 > valor1 + valor3 || valor3 > valor1 + valor2 ) {
    	   printf("ERRO !! VALORES NAO FORMAM UM TRIANGULO");
       } 

       else {
	   if (valor1 == valor2 == valor3) {
	      printf("Voce fez um triangulo equilatero");
	   }
	   else if (valor1 != valor2 != valor3 || valor1 != valor3 != valor2) {
	      printf("Voce fez um triangulo escaleno");
	   }
         }
       }

    else { 
       printf("ERRO!! EXISTE UM LADO NEGATIVO OU IGUAL A ZERO.");
    }
   
    return 0;
}