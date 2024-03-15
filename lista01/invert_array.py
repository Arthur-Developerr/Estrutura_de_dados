from array_ import array_invert


array_x = [int] * 10
for i in range(len(array_x)):
    number = int(input(f"Número na posição {i + 1}: "))
    array_x[i] = number


array_y = array_invert(array_x)

print(f"Vetor X: {array_x}")
print(f"Vetor Y: {array_y}")