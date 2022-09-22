#include <stdio.h>

int main()
{
    
    int vetor[10];
    int soma, X ,Y; 

    for(int i=0;i<10;i++)
    {
        printf("Insira o elemento na posicao %d do vetor: ", i);
        scanf("%d",&vetor[i]);
    }
    printf("Insira as posicoes X e Y: " );
    scanf("%d%d",  &X ,  &Y);
    
    soma = vetor[X] + vetor[Y];
    
    printf("%d", soma);
    return 0;
}