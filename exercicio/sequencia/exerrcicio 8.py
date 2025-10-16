hora = float(input("quanto você ganha à hora? "))

htrab = int(input("quantas horas você trabalha? "))

dias = int(input("quantos dias você trabalha por semana? "))

semanas = int(input("quantas semanas de trabalho? "))

salário = hora * htrab * dias * semanas

print("você ganha R$", salário)
