  #include <stdio.h>
#include <string.h>
int main()
{
    char vetor[30];
    int acharLadoDiamante(char letra, char* string);
    int dimas= 0 ,contEsquerda = 0 , contDireita = 0, dif= 0 ;
    
    gets(vetor);
    
    contEsquerda = acharLadoDiamante('<',vetor);
    contDireita = acharLadoDiamante('>',vetor);
    if (contDireita> contEsquerda){
        dif = contDireita - contEsquerda;
        dimas = contDireita - dif;
    }
    else{
        dif = contEsquerda - contDireita;  
        dimas = contEsquerda - dif;
    }
             
   printf("\n%d",dimas);
    return 0;
}
int acharLadoDiamante(char letra ,char* string){
    int qte = 0;
    for(int i = 0 ;string[i]; i++){
        if(string[i] == letra)
            qte++;
    }
    return qte;
}