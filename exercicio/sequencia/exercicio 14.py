limite_peso = 50
multa_kg = 4.00

peso_pescado = float(input("quantos kg de peixe você pescou?"))

if peso_pescado > limite_peso:
    excedente = peso_pescado - limite_peso
    valor_multa = excedente * multa_kg

    print(f"O excedente é {excedente}kg o valor da multa é R${valor_multa}")
else:
    print(f"Não excedeu o limite de {limite_peso}kg")