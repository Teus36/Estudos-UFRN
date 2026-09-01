#include <stdio.h>

int main (){
	int opcao;
	int valor1, valor2;	

	printf("Escolha uma opcao: \n");
	printf("1 - Soma\n");
	printf("2 - Subtracao\n");
	printf("3 - Multiplicacaco\n");
	printf("Opcao: ");
	scanf("%d", &opcao);

	printf("Digite 2 numeros: ");
	scanf("%d %d", &valor1, &valor2);

	switch (opcao) {
		case 1:
	  	    printf("Voce escolheu: Soma\n");
		    printf("%d + %d = %d", valor1, valor2, valor1 + valor2);
		    break;
		case 2:
	 	    printf("Voce escolheu: Subtracacao\n");
		    printf("%d - %d = %d", valor1, valor2, valor1 - valor2);
		    break;
		case 3:
		    printf("Voce escolheu: Multiplicacao\n");
		    printf("%d * %d = %d", valor1, valor2, valor1 * valor2);
                    break;
		default:
		    printf("Opcao inválida\n");
		}

		return 0;
}