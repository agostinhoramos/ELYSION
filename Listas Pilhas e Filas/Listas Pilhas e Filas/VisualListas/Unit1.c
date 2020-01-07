#include<stdio.h>
#include<conio.h>
void main() { (  ) 
int cont;
int tabuada;
int valor;
valor = 0;
printf("Introduza o valor da tabuada: ");
scanf("%i",&tabuada);
for(cont = 1;cont<=10;++cont){
valor = tabuada * cont;
printf("%i x %i = %i\n",tabuada,cont,valor);
}
getch();
}
