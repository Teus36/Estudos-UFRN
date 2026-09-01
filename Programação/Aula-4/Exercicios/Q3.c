#include <stdio.h>

int main() {
    float consumo;

    printf("Digite a quantidade KwH consumidos: ");
    scanf("%f", &consumo);	


    if (consumo > 0){
	if (consumo <= 100){
	   printf("A taxa de consumo deu R$%f (0,50)", consumo * 0.50);
        }
	else if (200 >= consumo && consumo >=101) {
	   printf("A taxa de consumo deu R$%f (0,75)", consumo * 0.75);
	}
	else if (500 >= consumo && consumo >= 201) {
           printf("A taxa de consumo deu R$%f (1,20)", consumo * 1.20);
	}
        else if (consumo > 500) {
      	   printf("A taxa de consumo deu R$%f (15/100)", consumo + (consumo *0.15));
        }
    }
    else {
	printf("Consumo inválido!!");
    }

    return 0;
}
