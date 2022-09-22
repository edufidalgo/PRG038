#include <stdio.h>
#include <math.h>
int main()
{
    int ponto1[] = {1,2};
    int ponto2[] =  {5,6};
    float resposta= 0;
    float distancia(int* ponto1, int* ponto2);
    resposta = distancia(ponto1,ponto2);
    printf("%f", resposta);
    
    
    return 0;
}

float distancia(int* ponto1, int* ponto2)
{
    int X1, X2, Y1 , Y2 ;
    float resposta;
    
    resposta = sqrt(pow((ponto2[0]-ponto1[0]),2) + pow((ponto2[1]-ponto1[1]),2));
    return resposta; 
    
}