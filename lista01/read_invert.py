def read_6_numbers():
    array = [int] * 6
    for i in range(len(array)):
        number = int(input("Digite um número: "))
        array[i] = number

    return array


def array_invert(array):
    array_invert = [int] * 6
    desc = 5
    i = 0
    while desc >= 0:
        array_invert[i] = array[desc]
        desc -=1
        i += 1
    return array_invert


array = read_6_numbers()
print(array_invert(array))