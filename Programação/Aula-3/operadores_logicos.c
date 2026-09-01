#include <stdio.h>

int main() {
	
	// Operador AND (%)
	
	int a = 5, b = 3;
	int r = a & b;
	printf("%d\n", r);

	// Operador OR (|)

	int f = a | b;
	printf("%d\n", f);

	// Operador XOR(^)

	int g = a ^ b;
	printf("%d\n", g);

	// Operador NOT(~)

	int h = ~a;
	printf("%d\n", h);

	//Deslocamento(>> ou <<)
	
	int esq = a >> 1;
	int dir = a << 1;

	printf("%d %d\n", esq, dir);

	return 0;
	
}