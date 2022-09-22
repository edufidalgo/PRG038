#include <stdio.h>
#include <string.h>
int main()
{
    char vetor[10];
    int ocorrencias(char letra, char* string);
    int qte = 0;
    
    gets(vetor);
    qte = ocorrencias('a',vetor);
   printf("\n%d",qte);
    return 0;
}
int ocorrencias(char letra ,char* string){
    int qte = 0;
    for(int i = 0 ;string[i]; i++){
        if(string[i] == letra)
            qte++;
    }
    return qte;
}