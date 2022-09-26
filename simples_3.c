#include <stdio.h>
 int* encontra_primo(int lista[], int tamanho) ;
 int tamanho;
int main()
{ 
    // CODIGO NO MAIN PARA TESTES.
 scanf("%d", &tamanho);
 int lista[tamanho] , *primos;

 for(int i = 0; i<tamanho ; i++){
     scanf("%d", &lista[i]);
 }
 
  
 primos = encontra_primo(lista, tamanho);
 
 for(int i = 0; i<tamanho ; i++){
     printf("\n%d", primos[i]);
 }
   return 0;
}
  /*função para encontrar primos em uma lista.

      Parametros: (int* lista, int tamanho)
      ----------
      vetor de numeros a serem testados.
      tamanho do vetor.

      Retorna: int* primos
      -------
      Um vetor contendo apenas os números que forem primos da lista de entrada
  */
int* encontra_primo(int lista[] , int tamanho) {
    
   static int primos[100];
   int primo, k = 0;

    
   for ( int i = 0; i <tamanho; i++)
   {
       primo = 1;
    if (lista[i] == 0 || lista[i] == 1)
        primo = 0;
               
    for (int j = 2; j <= lista[i] / 2; j++) 
        {
            if ( lista[i] % j == 0)
            {
                primo = 0;
                break;
            }
        }   
    if(primo == 1){
        primos[k] = lista[i];
        k++;
    }
   }

   return primos;
}