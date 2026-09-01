#include <stdio.h> 


int main (){
	int temperatura;

	printf("Digite a temperatura atual (em graus Celsius): ");
	scanf("%d", &temperatura);
	
	//1º 'if' inicial
	if (temperatura >= 35) {
		printf("Alerta: Muito quente! Beba bastante agua.\n");
	}	

	//1º 'elfe if'
	else if (temperatura >= 25) {
		printf("Clima quente. Dia bom para ir a praia.\n");
	}
	//2º 'else if'

	else if (temperatura >= 15) {
		printf("Clima agradavel\n");
	}

	//3º 'else if'
	else if (temperatura >= 5) {
		printf("Clima frio. Nao esqueca o casaco.\n");
	}

	//1º 'else' final
	else {
		printf("Alerta: Muito frio! Fique aquecido.\n");
	}

	return 0;
}