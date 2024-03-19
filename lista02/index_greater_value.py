def get_index_greater_value(number_array):
    #função que retorna o maior valor e seu indice
    greater_number = number_array[0][0]
    pos_i = 0
    pos_j = 0
    for i in range(1, len(number_array)):
        for j in range(1, len(number_array)):
            if number_array[i][j] > greater_number:
                greater_number = number_array[i][j]
                pos_i = i
                pos_j = j
    return [greater_number, pos_i, pos_j]
                
            

number_array = [int] * 4 

for c in range(len(number_array)):
    number_array[c] = [int] * 4

for i in range(len(number_array[0])):
    for j in range(len(number_array[1])):
        number = int(input("Digite um número: "))
        number_array[i][j] = number


list = get_index_greater_value(number_array)

greater_value = list[0]
pos_i = list[1]
pos_j = list[2]
 
print(f"O maior valor do vetor é {greater_value} e esta na posição ({pos_i},{pos_j})")