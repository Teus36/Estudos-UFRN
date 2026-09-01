#include <stdio.h>

int main() {
    int ano;

    printf("Digite um ano: ");
    scanf("%d", &ano);

    if ((ano & 3) == 0 && (ano % 100) != 0 || (ano % 400) == 0){
	printf("Ano bissexto");
    }
    else {
	printf("Ano não bissexto");
    }

    return 0;
}
	