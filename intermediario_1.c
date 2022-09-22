#include <stdio.h>
#include <math.h>
int main()
{
    int X1,Y1,X2,Y2,X3,Y3;
    int produtoEsc, modulo1, modulo2;
    double resposta;
    printf("insira as coordenadas dos 3 pontos, respectivamente: ");
    scanf("%d%d%d%d%d%d", &X1,&Y1,&X2,&Y2,&X3,&Y3);
    X1 = X1 - X2;
    Y1 = Y1 - Y2;
    X3 = X3 - X2;
    Y3 = Y3 - Y2;
    produtoEsc = X1*X3 + Y1*Y3;
    modulo1 = sqrt(X1*X1 + Y1*Y1);
    modulo2= sqrt(X3*X3 + Y3*Y3);
    
    resposta = acos(produtoEsc/(modulo1*modulo2));
    
    printf("%lf radianos", resposta);
}