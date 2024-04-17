matriz_alunos = [str] * 5
vetor_gabarito = ['a', 'c', 'd', 'c', 'a', 'b', 'd', 'b', 'c', 'a']
vetor_resultado = []

indice_vetor_gabarito = 0
pontos = 0

for i in range(len(matriz_alunos)):
  matriz_alunos[i] = [str] * 10


for l in range(len(matriz_alunos)):
  for c in range(len(matriz_alunos[0])):
    questao = str(input(f"Digite a alternativa da questão {c + 1} do aluno{l + 1}: "))
    matriz_alunos[l][c] = questao

for k in range(len(matriz_alunos)):
  for j in range(len(matriz_alunos[0])):
    if matriz_alunos[k][j] == vetor_gabarito[indice_vetor_gabarito]:
      pontos += 1
      indice_vetor_gabarito += 1
  vetor_resultado.append(pontos)
  pontos = 0
  indice_vetor_resultado = 0



print(f"As notas de todos os alunos são: {matriz_alunos}")
for n in range(len(vetor_resultado)):
  print(f"O aluno{n + 1} tirou {vetor_resultado[i]}")