from random import randint


def buscar_matriz(matriz, valor):
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if matriz[i][j] == valor:
        return True
  return False

def criar_cartela():
  matriz_bingo = [int] * 5
  for i in range(len(matriz_bingo)):
    matriz_bingo[i] = [int] * 5

  return matriz_bingo


def preencher_cartela():
  matriz_bingo = criar_cartela()

  for i in range(len(matriz_bingo)):
    for j in range(len(matriz_bingo)):
      num_aleatorio = randint(0, 99)
      if buscar_matriz(matriz_bingo, num_aleatorio) == False:
        matriz_bingo[i][j] = num_aleatorio
      else:
        while True:
          novo_numero = randint(0,99)
          if buscar_matriz(matriz, novo_numero) == False:
           matriz_bingo[i][j] = novo_numero
           break

  return matriz_bingo


print(preencher_cartela())