def vetor_numbers_squared(array):
    array_squared = [int] * 10
    for i in range(len(array)):
        array_squared[i] = array[i] ** 2
        
    return array_squared


array = [int] * 10
for i in range(10):
    number = int(input("Digite um número: "))
    array[i] = number

print(f'O vetor inicial é {array}')
print(f'O vetor ao quadrado é {vetor_numbers_squared(array)}')


