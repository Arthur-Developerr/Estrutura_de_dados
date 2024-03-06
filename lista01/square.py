def read_10_numbers():
    array = [int] * 10
    for i in range(10):
        number = int(input("Digite um número: "))
        array[i] = number

    return array


def vetor_numbers_squared(array):
    array_squared = [int] * 10
    for i in range(len(vetor)):
        array_squared[i] = array[i] ** 2
        
    return array_squared


vetor = read_10_numbers()
print(f'O vetor inicial é {vetor}')
print(f'O vetor ao quadrado é {vetor_numbers_squared(vetor)}')


