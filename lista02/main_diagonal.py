def insert_on_zero_ones_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 0


number_array = [int] * 5

for c in range(len(number_array)):
    number_array[c] = [int] * 5


insert_on_zero_ones_array(number_array)
print(number_array)


