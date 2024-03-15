def multiplication_row_column(array):
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = (i + 1) * (j + 1)


number_array = [int] * 5

for c in range(len(number_array)):
    number_array[c] = [int] * 5



multiplication_row_column(number_array)
print(number_array)