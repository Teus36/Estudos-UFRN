#include <stdio.h> 

int main (){
    int id_produto;
    int quantidade;
    int sobremesa;
    float valor_produtos;
    float valor_sobremesa = 0;
    float desconto = 0;
    float soma;

    printf("============ MENU ============\n");
    printf("1 - Hamburguer ........ R$ 18,00\n");
    printf("2 - X-Salada .......... R$ 22,00\n");
    printf("3 - X-Bacon ........... R$ 25,00\n");
    printf("4 - Batata Frita ...... R$ 12,00\n");
    printf("5 - Refrigerante ...... R$  7,00\n");

    printf("Escolha uma das opcoes acima: ");
    scanf("%d", &id_produto);
    printf("Quanto voce ira querer?: ");
    scanf("%d", &quantidade);
    printf("Deseja adicionar sobremesa? Digite 1 para sim e 0 para não: ");
    scanf("%d", &sobremesa);


    if (id_produto <= 5 && id_produto > 0){
	switch (id_produto) {
	   case 1:
	      valor_produtos = quantidade * 18;
	      break;
	   case 2:
	      valor_produtos = quantidade * 22;
	      break;
	   case 3:
	      valor_produtos = quantidade * 25;
	      break;
	   case 4:
	      valor_produtos = quantidade * 12;
	      break;
	   case 5:
	      valor_produtos = quantidade * 7;
	      break;
	   default:
	      break;
           } 

         soma = valor_produtos;
     
         if (sobremesa == 1) {
	    soma = soma + valor_sobremesa;
         }	   

         if (soma > 100) {
   	    desconto = soma * 0.10;
         }

         else if (soma >= 50 && soma <= 100) {
	    desconto = soma * 0.05;
         }
	
         soma = soma - desconto;

	 printf("\n============ PEDIDO ============\n");

         switch (id_produto) {
            case 1:
                printf("Produto escolhido: Hamburguer\n");
                break;
            case 2:
                printf("Produto escolhido: X-Salada\n");
                break;
            case 3:
                printf("Produto escolhido: X-Bacon\n");
                break;
            case 4:
                printf("Produto escolhido: Batata Frita\n");
                break;
            case 5:
                printf("Produto escolhido: Refrigerante\n");
                break;
         }

         printf("Quantidade: %d\n", quantidade);
         printf("Valor dos produtos: R$ %.2f\n", valor_produtos);
         printf("Valor da sobremesa: R$ %.2f\n", valor_sobremesa);
         printf("Desconto: R$ %.2f\n", desconto);
         printf("Valor final do pedido: R$ %.2f\n", soma);
    }

    else {
	printf("ID INVÁLIDO!!");
    }

    return 0;
}