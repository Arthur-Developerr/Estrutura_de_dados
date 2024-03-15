array_numbers = [int] * 4
greater_than_10 = 0
list_greater_than_10 = list()

for i in range(len(array_numbers)):
    array_numbers[i] = [int] * 4


for l in range(len(array_numbers[0])):
    for c in range(len(array_numbers[1])):
        number = int(input("numero: ")) 
        array_numbers[l][c] = number
        if array_numbers[l][c] > 10:
            greater_than_10 +=1
            list_greater_than_10.append(number)


print(f"A matriz digitada foi: {array_numbers}")
print(f"Nesta matriz há {greater_than_10} números maiores que 10")
print(f"Os números da matriz que são maiores que 10 são: {list_greater_than_10}")

