

#Documentação estilo NumPy, com docstrings

def ameaca_cavalo(p):

  """função que identifica as casas do tabuleiro ameaçadas pelo cavalo

      Parametros
      ----------
      p : tupla
      posição do cavalo no tabuleiro em coordenadas cartesianas (x,y)

      Retorna
      -------
      posicoes_ameacadas : lista de tuplas
      lista de posições ameaçadas pela peça na posição p

  """

  posicoes_ameacadas = []
  for i in [-1, -2, 1, 2]:
    if i == -1 or i == 1:
       for j in [-2, 2]:
         posicoes_ameacadas.append((p[0] + i, p[1] + j))
    if i == -2 or i == 2:
       for j in [1, -1]:
         posicoes_ameacadas.append((p[0] + i, p[1] + j))
      

  return posicoes_ameacadas

def ameaca_torre(p):

  """função que identifica as casas do tabuleiro ameaçadas pela torre

      Parametros
      ----------
      p : tupla
      posição da torre no tabuleiro em coordenadas cartesianas (x,y)

      Retorna
      -------
      posicoes_ameacadas : lista de tuplas
      lista de posições ameaçadas pela peça na posição p

      
  """

  posicoes_ameacadas = []
  for i in range(-7,8):
    posicoes_ameacadas.append((p[0] + i, p[1]))
  for j in range(-7,8):
    posicoes_ameacadas.append((p[0], p[1] + j))

  return posicoes_ameacadas

def ameaca_bispo(p):

  """função que identifica as casas do tabuleiro ameaçadas pelo bispo

      Parametros
      ----------
      p : tupla
      posição do bispo no tabuleiro em coordenadas cartesianas (x,y)
      
      Retorna
      -------
      posicoes_ameacadas : lista de tuplas
      lista de posições ameaçadas pela peça na posição p

      
  """

  posicoes_ameacadas = []
  for i in range(-7,8):
    posicoes_ameacadas.append((p[0] + i, p[1] + i))
  for j in range(-7,8):
    posicoes_ameacadas.append((p[0] - j, p[1] + j))

  return posicoes_ameacadas

def ameaca_rainha(p):

  """função que identifica as casas do tabuleiro ameaçadas pela rainha

      Parametros
      ----------
      p : tupla
      posição da rainha no tabuleiro em coordenadas cartesianas (x,y)

      Retorna
      -------
      posicoes_ameacadas : lista de tuplas
      lista de posições ameaçadas pela peça na posição p

      
  """

  posicoes_ameacadas_1 = ameaca_torre(p)
  posicoes_ameacadas_2 = ameaca_bispo(p)
  posicoes_ameacadas = posicoes_ameacadas_1 + posicoes_ameacadas_2

  return posicoes_ameacadas

def ameaca_peao(p, cor):

  """função que identifica as casas do tabuleiro ameaçadas pelo peão

      Parametros
      ----------
      p : tupla
      posição do peão no tabuleiro em coordenadas cartesianas (x,y)
      cor : string
      cor da peça na posição p. Valor pode ser "branco" ou "preto". Pretas
      avançam na direção +x, enquanto brancas avançam na direção -x

      Retorna
      -------
      posicoes_ameacadas : lista de tuplas
      lista de posições ameaçadas pela peça na posição p

      
  """
  posicoes_ameacadas = []
  if cor == "preto":
    posicoes_ameacadas.append((p[0]+1, p[1]+1))
    posicoes_ameacadas.append((p[0]+1, p[1]-1))
  if cor == "branco":
    posicoes_ameacadas.append((p[0]-1, p[1]+1))
    posicoes_ameacadas.append((p[0]-1, p[1]-1))

  return posicoes_ameacadas

def ameaca_rei(p):

  """função que identifica as casas do tabuleiro ameaçadas pelo rei

      Parametros
      ----------
      p : tupla
      posição do rei no tabuleiro em coordenadas cartesianas (x,y)

      Retorna
      -------
      posicoes_ameacadas : lista de tuplas
      lista de posições ameaçadas pela peça na posição p

      
  """
  posicoes_ameacadas = []
  posicoes_ameacadas.append((p[0]-1, p[1]+1))
  posicoes_ameacadas.append((p[0]-1, p[1]-1))
  posicoes_ameacadas.append((p[0]+1, p[1]+1))
  posicoes_ameacadas.append((p[0]+1, p[1]-1))
  posicoes_ameacadas.append((p[0]+1, p[1]))
  posicoes_ameacadas.append((p[0]-1, p[1]))
  posicoes_ameacadas.append((p[0], p[1]-1))
  posicoes_ameacadas.append((p[0], p[1]+1))

  return posicoes_ameacadas

def parse_ascii_main(jogos):

  """
  Função principal do programa. Itera sobre os jogos de xadrez e
  retorna um aviso quando o rei está em cheque

  Parametros
  ----------
  jogos : lista de listas de listas de strings
  É uma lista de jogos de xadrez, representados por matrizes 8x8 de caracteres
  nessas matrizes, as letras "Rr Kk Qq Nn Bb Pp" representam a torre, o rei,
  a rainha, o cavalo, o bispo e o peão, respectivamente. Letras maiúsculas
  representam peças brancas, enquanto minúsculas são pretas.
  
  """

  n = 0
  for jogo in jogos:
    n += 1
    #definir listas de coordenadas
    coord_rei_branco = []
    coord_rei_preto = []
    coord_peao_branco = []
    coord_peao_preto = []
    coord_bispo_branco = []
    coord_bispo_preto = []
    coord_torre_branco = []
    coord_torre_preto = []
    coord_rainha_branco = []
    coord_rainha_preto = []
    coord_cavalo_branco = []
    coord_cavalo_preto = []

    #tabelas de ameaca: listas de casas ameaçadas por todas as peças de cada cor

    tabela_branco = []
    tabela_preto = []

    #transformar ascii em listas de coordenadas

    for i in range(0, 8):
      for j in range(0, 8):
        if jogo[i][j] == ".":
          continue
        if jogo[i][j] == "p":
          coord_peao_preto.append((i,j))
        if jogo[i][j] == "P":
          coord_peao_branco.append((i,j))
        if jogo[i][j] == "r":
          coord_torre_preto.append((i,j))
        if jogo[i][j] == "R":
          coord_torre_branco.append((i,j))
        if jogo[i][j] == "k":
          coord_rei_preto.append((i,j))
        if jogo[i][j] == "K":
          coord_rei_branco.append((i,j))
        if jogo[i][j] == "q":
          coord_rainha_preto.append((i,j))
        if jogo[i][j] == "Q":
          coord_rainha_branco.append((i,j))
        if jogo[i][j] == "n":
          coord_cavalo_preto.append((i,j))
        if jogo[i][j] == "N":
          coord_cavalo_branco.append((i,j))
        if jogo[i][j] == "b":
          coord_bispo_preto.append((i,j))
        if jogo[i][j] == "B":
          coord_bispo_branco.append((i,j))
    
    #inserir coordenadas processadas do ascii em tabelas de ameaca
    for peca in coord_rei_preto:
      for coord in ameaca_rei(peca):
        tabela_preto.append(coord)
    
    for peca in coord_rei_branco:
      for coord in ameaca_rei(peca):
        tabela_branco.append(coord)
    
    for peca in coord_cavalo_branco:
      for coord in ameaca_cavalo(peca):
        tabela_branco.append(coord)
    
    for peca in coord_cavalo_preto:
      for coord in ameaca_cavalo(peca):
        tabela_preto.append(coord)

    for peca in coord_rainha_preto:
      for coord in ameaca_rainha(peca):
        tabela_preto.append(coord)
    
    for peca in coord_rainha_branco:
      for coord in ameaca_rainha(peca):
        tabela_branco.append(coord)
    
    for peca in coord_bispo_branco:
      for coord in ameaca_bispo(peca):
        tabela_branco.append(coord)
    
    for peca in coord_bispo_preto:
      for coord in ameaca_bispo(peca):
        tabela_preto.append(coord)
    
    for peca in coord_torre_preto:
      for coord in ameaca_torre(peca):
        tabela_preto.append(coord)
    
    for peca in coord_torre_branco:
      for coord in ameaca_torre(peca):
        tabela_branco.append(coord)
    
    for peca in coord_peao_branco:
      for coord in ameaca_peao(peca, "branco"):
        tabela_branco.append(coord)
    
    for peca in coord_peao_preto:
      for coord in ameaca_peao(peca, "preto"):
        tabela_preto.append(coord)
    
    #utilizar a função set para remover coordenadas repetidas
    tabela_preto = set(tabela_preto)
    tabela_branco = set(tabela_branco)

    #encontrar posição do rei. Se não for encontrada, retornar erro por ausencia
    try:
      rei_preto = coord_rei_preto[0]
    except:
      rei_preto = "error"
      print("Jogo #{}: Não tem rei preto no tabuleiro".format(n))
    try:
      rei_branco = coord_rei_branco[0]
    except:
      rei_branco = "error"
      print("Jogo #{}: Não tem rei branco no tabuleiro".format(n))


    #produzir mensagem
    if rei_preto in tabela_branco:
      print("Jogo #{}: rei preto esta em cheque.".format(n))

    if rei_branco in tabela_preto:
      print("Jogo #{}: rei branco esta em cheque.".format(n))

#Teste

tab = [[['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'K', '.', '.', '.', '.'],
 ['.', '.', '.', 'P', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', 'k', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.']],[['.', '.', 'r', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'K', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.']],[['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'K', '.', '.', '.', '.'],
 ['.', '.', '.', 'q', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', 'k', '.'],
 ['.', '.', '.', '.', '.', 'P', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.']]]
parse_ascii_main(tab)

help(ameaca_cavalo)

