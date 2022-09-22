
def ameaca_cavalo(p):
  #p é uma tupla
  posicoes_ameacadas = []
  for i in [-1, -2, 1, 2]:
    for j in [-1, -2, 1, 2]:
      posicoes_ameacadas.append((p[0] + i, p[1] + j))

  return posicoes_ameacadas

def ameaca_torre(p):
  #p é uma tupla
  posicoes_ameacadas = []
  for i in range(-7,8):
    posicoes_ameacadas.append((p[0] + i, p[1]))
  for j in range(-7,8):
    posicoes_ameacadas.append((p[0], p[1] + j))

  return posicoes_ameacadas

def ameaca_bispo(p):
  #p é uma tupla
  posicoes_ameacadas = []
  for i in range(-7,8):
    posicoes_ameacadas.append((p[0] + i, p[1] + i))
  for j in range(-7,8):
    posicoes_ameacadas.append((p[0] - j, p[1] + j))

  return posicoes_ameacadas

def ameaca_rainha(p):
  #p é uma tupla
  posicoes_ameacadas_1 = ameaca_torre(p)
  posicoes_ameacadas_2 = ameaca_bispo(p)
  posicoes_ameacadas = posicoes_ameacadas_1 + posicoes_ameacadas_2

  return posicoes_ameacadas

def ameaca_peao(p, cor):
  posicoes_ameacadas = []
  #p é uma tupla
  #cor é a string da cor das peças do jogador ("preto" ou "branco"). Será padronizada a seguinte orientação:
  #As pretas avançam para baixo (+x) (minúsculas). As brancas avançam para cima (-x) (maiúsculas)
  if cor == "preto":
    posicoes_ameacadas.append((p[0]+1, p[1]+1))
    posicoes_ameacadas.append((p[0]+1, p[1]-1))
  if cor == "branco":
    posicoes_ameacadas.append((p[0]-1, p[1]+1))
    posicoes_ameacadas.append((p[0]-1, p[1]-1))

  return posicoes_ameacadas

def ameaca_rei(p):
  posicoes_ameacadas = []
  #p é uma tupla
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
  n = 1
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

    #tabelas de ameaca

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
      for coord in ameaca_peao(peca):
        tabela_branco.append(coord)
    
    for peca in coord_peao_preto:
      for coord in ameaca_peao(peca):
        tabela_preto.append(coord)
    
    tabela_preto = set(tabela_preto)
    tabela_branco = set(tabela_branco)

    rei_preto = coord_rei_preto[0]
    rei_branco = coord_rei_branco[0]

    if rei_preto in tabela_branco:
      print("Jogo #{}: rei preto esta em cheque.".format(n))

    if rei_branco in tabela_preto:
      print("Jogo #{}: rei branco esta em cheque.".format(n))



