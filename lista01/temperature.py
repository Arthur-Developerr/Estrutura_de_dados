import array_ as array

array_avarage_temp_month = [float] * 12
array_name_months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
                     "Setembro", "Outubro", "Novembro", "Dezembro"]

def avarage_up(vetor):
    avarage = array.avarage_array(array_avarage_temp_month)
    for i in range(len(vetor)):
        if vetor[i] > avarage:
            print(f"o mês de {array_name_months[i]} teve média de {array_avarage_temp_month[i]}")


for i in range(len(array_avarage_temp_month)):
    avarage_temp_month = float(input(f"Digite a temperatura média de {array_name_months[i]}: "))
    array_avarage_temp_month[i] = avarage_temp_month


print(f"A média anual das temperaturas é: {array.avarage_array(array_avarage_temp_month)}")
print("Os meses que tiveram as temperaturas acima da média são:")
avarage_up(array_avarage_temp_month)