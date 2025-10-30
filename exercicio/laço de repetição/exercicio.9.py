numero = int(input("Digite um número para ver a tabuada (entre 1 e 10): "))

if 1 <= 10:
    print(f"Tabuada de {numero}:")

    for i in range(1,11):

        resultado = numero * i

        print(f" {numero}X {i} = {resultado}")
