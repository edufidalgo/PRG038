
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
  /*funcao para identificar numeros perfeitos

      Parametros (int numero)
      ----------
      recebe o numero a ser conferido

      Retorna  (int 0 ou 1)
      -------
      retorno 1 caso seja perfeito, 0 caso nao.

      
  */
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
