nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))

soma = nota1 + nota2
media = soma /2
if media >= 7:
    print("Parabéns você foi aprovado")
elif media >=6.5:
    print("Cuidado, você passou pelo conselho")
elif media >= 7.5:
    print("Você está em exame!!!")
else:
    print(" Parabéns, você foi reprovado")
if media <= 10:
    print("Você é o aluno destaque")




