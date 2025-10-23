print("M - Masculino | F - Feminino | O -outros")
sexo= (input("Digite a letra correspondente ao seu sexo: "))

if sexo == "M" or sexo == "m":
    print("Você é do sexo Masculino")
elif sexo == "F" or sexo == "f":
    print("Você é do sexo Feminino")
else:
    print("Você preferiu não informar")

match sexo:
    case "M":
        print("Sexo masculino")
    case "m":
        print("Sexo masculino")
    case "F":
        print("Sexo feminino")
    case "f":
        print("Sexo feminino")
    case _:
        print("Indefinido")
