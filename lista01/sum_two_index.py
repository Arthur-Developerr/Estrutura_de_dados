def read_8_numbers():
    array = [int] * 10
    for i in range(8):
        number = int(input("Digite um número: "))
        array[i] = number

    return array


def sum_two_index(array, x, y):
    if x <= 8 and y <= 8:
        return array[x] + array[y]
    else:
        raise IndexError


array = read_8_numbers()
x = int(input("Digite a posição X: "))
y = int(input("Digite a posição Y: "))
print(sum_two_index(array, x, y ))





