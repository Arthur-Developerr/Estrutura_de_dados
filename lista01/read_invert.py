from array_ import array_invert

array = [int] * 6
for i in range(len(array)):
        number = int(input("Digite um número: "))
        array[i] = number

print(array_invert(array))