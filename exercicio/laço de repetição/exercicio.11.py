idades= []
idade = 0
while idade != -1:
    idade = int(input("Digite o valor da idade: "))
    if idade > 0:
        idades.append(idade)


soma = 0
for idade in idades:
    soma = soma + idade

media = soma / len(idades)

print(f"As idades foram {idades}")
print(f"A média é {media}")

if media <= 25:
    print("A turma é Jovem")
elif media <= 60:
    print("A turma é Adulta")
else:
    print("A turma é idosa")