#include <stdio.h>

int main() {
   float saldo = 1000;
   float deposito;
   float saque;
   float limite;
   int opcao;

   printf("========== CAIXA ELETRONICO ==========\n");
   printf("1 - Consultar saldo\n");
   printf("2 - Depositar\n");
   printf("3 - Sacar\n");
   printf("4 - Verificar limite\n");
   printf("5 - Encerrar\n");

   printf("Escolha uma das opcoes acima: ");
   scanf("%d", &opcao);

   switch (opcao) {
	case 1:
	    printf("Saldo disponivel: R$%.2f", saldo);
	    break;
	case 2:
	    printf("Informe o valor do deposito: R$");
	    scanf("%f", &deposito);

	    saldo = saldo + deposito;

	    printf("Voce depositou: R$%.2f", deposito);
	    break;
	case 3:
	    printf("Informe o valor do saque: R$");
	    scanf("%f.2f", &saque);

	    if (saque < 0) {
	     	printf("ERRO!! VOCÊ NAO PODE SACAR UM VALOR NEGATIVO");
	    }
	    else if (saque > saldo) {
		printf("ERRO!! SALDO INSUFICIENTE");
	    }
	    else {
		saldo = saldo - saque;
		printf("Saque de R$%.2f realizado com sucesso!!", saque);
	    }
	    break;
	case 4:
	    limite = saldo * 0.3;
	    printf("Limite disponivel para saque: R$%.2f", limite);
	    break;
	case 5:
	    break;
	default:
	    printf("Opcao inválida!!");
   }

   return 0;
}