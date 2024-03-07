import array_ as array


array_age = [int] * 5
array_height = [float] * 5
for i in range(len(array_age)):
    age = int(input("Digite a idade: "))
    height = float(input("Digite a altura: "))
    array_age[i] = age
    array_height[i] = height

print(f"A média das idades é: {array.avarage_array(array_age)}")
print(f"A médias das alturas é: {array.avarage_array(array_height)}")
print(f"O mais novo é: {array.smaller_array(array_age)}")
print(f"O mais velhor é: {array.greatest_array(array_age)}")
print(f"O mais alto é: {array.greatest_array(array_height)}")
print(f"O mais baixo é: {array.smaller_array(array_height)}")