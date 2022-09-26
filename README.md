# PRG038
muito simples 1.
      Recebe-se as duas coordenadas de cada ponto, e é tirado a raiz quadrada da soma dos quadrados da diferença das            coordenadas em cada eixo.
      
muito simples 2.
      Foi aplicada a fórmula da conversão de fahrenheit para celsius, que é subtrair 32 e dividir por 1,8.
      
simples 1.
      Recebe-se cada elemento do vetor, um a um, pelo console. Depois, recebe-se no input  as posições X e Y. É aplicada a soma dos elementos no vetor nas posições X e Y.
      
simples 2.
      O operador % (retorna o resto da divisão) é usado na função, que adiciona a soma caso ele seja zero. se a soma for igual ao input, é retornado 1 (true).
      
simples 3.
      A função recebe um vetor de inteiros, e o tamanho dessa lista, pre-definido pelo usuario. Num loop conferindo cada um dos elementos: Confere-se caso sejam 0 ou 1, o que os faz nao primos. Depois, num loop que começa em 2 e vai até a metade do valor do elemento conferido, checa-se a divisibilidade do elemento. Caso alguma seja possivel, ele é marcado como nao primo. No final desse processo, caso o marcador de primo seja 1, o elemento em questao sera adicionado ao vetor de primos, que será retornado.
      
simples 4.
      Utiliza-se a função "gets()" para receber uma string como input. Depois, em um loop, é conferido cada elemento a igualdade com o char escolhido, e contado a cada ocorrencia.
      
intermediario 1.
      Recebe-se 6 coordenadas no input, duas para cada ponto, e considera-se as duas do meio como o ponto de encontro dos dois vetores que criam o ângulo. Retira-se as quantidades em X e Y dos pontos 1 e 3, para trazer os vetores ao ponto 0. Basta aplicar a fórmula para o ângulo entre vetores.

intermediario 2.
      Utilizando-se logica similar ao ex simples_3, é criado na função um inteiro para marcar um numero repetido, um inteiro k para guardar o tamanho da nova lista. Após isso, confere-se, para cada numero da lista de entrada, sua igualdade com todos os elementos da nova lista. Ao final, a nova lista terá zeros nos espaços que nao forem utilizados.
      
dificil 1. 
      Foi utilizado o código para reconhecer repetições da questão simples 4, e apenas foi contado a quantidade de metades para esquerda e para a direita dos diamantes. 
      Consegue-se a diferença entre as duas quantidades, subtraindo-a do maior numero de lados. Essa é a quantidade de pares.
      
dificil 2
       Para este problema foi utilizado python. O tabuleiro é uma matriz 8x8. Foram definidas funções que identificam, a partir da posição de cada peça, quais casas estão sendo ameaçadas, ou seja, colocadas em cheque pela peça. Depois disso a função principal itera sobre a lista de n jogos, definida como um tensor nx8x8 de strings de um só caractere. Nesse processo, o programa usa as funções previamente definidas para listar todas as posições em que um rei poderia estar em cheque e verifica se o rei está em uma dessas posições. 
       
      
