def search_array_dimensional(array_number, value):
    for i in range(len(array_number[0])):
        for j in range(len(array_number[1])):
            if array_number[i][j] == value:
                return [i, j]
    return "não encontrado"
    

array_number = [int] * 5
for c in range(len(array_number)):
    array_number[c] = [int] * 5


for i in range(len(array_number[0])):
    for j in range(len(array_number[1])):
        number = int(input("Digite um número: "))
        array_number[i][j] = number

value = int(input("Digite o valor que deseja buscar: "))

position = search_array_dimensional(array_number, value)
