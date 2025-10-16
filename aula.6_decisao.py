nota1 = 3
nota2 = 3
nota3 = 3
nota4 = 3

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"Média {media}")

if media >= 7:
    print("Parabéns, você foi aprovado")
elif media >= 6.5:
    print("Cuidado, você passou pelo conselho")
elif media >= 7.5:
    print("Você está em exame!!!")
else:
    print(" Parabéns, você foi reprovado")
