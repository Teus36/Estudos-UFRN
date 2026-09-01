#include <stdio.h>

int main() {
   int a;
   int b;
   int opcao;
   int resultado;

   printf("Digite o valor de A: ");
   scanf("%d", &a);

   printf("Digite o valor de B: ");
   scanf("%d", &b);


   printf("1 - E bit a bit (&)\n");
   printf("2 - OU bit a bit (|)\n");
   printf("3 - OU exclusivo (^)\n");
   printf("4 - Deslocamento a esquerda (<<)\n");
   printf("5 - Deslocamento a direita (>>)\n");

   printf("Agora escolha uma das operacoes acima: ");
   scanf("%d", &opcao);

   switch (opcao) {
        case 1:
            resultado = a & b;
            break;
        case 2:
            resultado = a | b;
            break;
        case 3:
            resultado = a ^ b;
            break;
        case 4:
            resultado = a << b;
            break;
        case 5:
            resultado = a >> b;
            break;
        default:
            printf("Operacao invalida\n");
            return 0;
    }

   printf("Resultado em decimal: %d\n", resultado);
   printf("Resultado em hexadecimal: %x\n", resultado);

   return 0;
}