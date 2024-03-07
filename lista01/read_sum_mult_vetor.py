def vetor_soma(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma


def vetor_multi(vetor):
    multi = vetor[0]
    for i in range(1, len(vetor)):
        multi = multi * vetor[i]
    return multi


array = [int] * 5
for i in range(len(array)):
    number = int(input("Digite um número: "))
    array[i] = number


print(f"Soma de todos os valores do vetor é: {vetor_soma(array)}")
print(f'A multiplicação dos valores do vetor é {vetor_multi(array)}')
print(f"O vetor é {array}")