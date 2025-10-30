base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = base

for contador in range(1,expoente + 1):
    resultado = resultado * base

    print(f"{base}^{expoente} = {resultado}")