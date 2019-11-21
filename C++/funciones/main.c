#include <stdio.h>
#include <stdlib.h>
#include "biblioteca.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int sumar(int a, int b){
	int c = a + b;
	return c;
}

int main(int argc, char *argv[]) {
	printf("La suma de 3 y 4 es: %d \n", sumar(3,4));
	printf("\n");
	pinta_A();
	return 0;
}
