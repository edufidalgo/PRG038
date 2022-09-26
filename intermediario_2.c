#include <stdio.h>
 int* eliminar_repeticoes(int lista[], int tamanho) ;
 int tamanho;
int main()
{ 
    // CODIGO NO MAIN PARA TESTES.
 scanf("%d", &tamanho);
 int lista[tamanho] , *novaLista;

 for(int i = 0; i<tamanho ; i++){
     scanf("%d", &lista[i]);
 }
 
  
 novaLista = eliminar_repeticoes(lista, tamanho);
 
 for(int i = 0; i<tamanho ; i++){
     printf("\n%d", novaLista[i]);
 }
   return 0;
}
  /*funcao para retornar lista nem numeros repetidos.

      Parametros: (int* lista, int tamanho)
      ----------
      vetor de numeros a serem testados.
      tamanho do vetor.

      Retorna (int* novaLista)
      -------
      Um vetor contendo apenas numeros sem repeticoes na ultima lista, mais uma sequencia de zeros
      ocupando os espacos nao ocupados.
  */
int* eliminar_repeticoes(int lista[] , int tamanho) {
    
   static int novaLista[100];
   int igual, k = 0 ;

    
   for ( int i = 0; i < tamanho; i++) 
   {
       igual = 0;
        for(int j = 0 ; j < tamanho; j++){
            if(lista[i] == novaLista[j]){
                igual = 1;
                break;
            }
        }
        if(igual == 0){
            novaLista[k]=lista[i];
            k++;
        }
   }
   
   return novaLista;
}