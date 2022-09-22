
#include <stdio.h>
#include <math.h>

int main()
{
   
    int perfeito(int numero);
    int numero, resultado;
    
    
    scanf("%d", &numero);
    resultado = perfeito(numero);
    printf("%d", resultado);
    
    return 0;
}
int perfeito(int numero)
{
    int soma= 0;
    for ( int i = numero/2; i > 0; i--)
    {
      if( numero % i == 0 )
      {
          soma += i;
      }
    }
    if( soma == numero)
        return 1;
    else 
        return 0;    
}