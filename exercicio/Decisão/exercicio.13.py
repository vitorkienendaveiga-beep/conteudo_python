import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a == 0:
    print("Essa equação não é de segundo grau")
    exit(1)

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("O delta é negativo, portanto não é possivel calcular a raiz")
    exit(1)

if delta == 0:
    print("O delta possui apenas uma riaz real")
    raiz = 0
    x = (b * -1) / (2 * a)
    print("O valor de x é ")
else:
    raiz = math.sqrt(delta)
    xa = ((b * -1) + raiz) / (2 * a)
    xb = ((b * -1)- raiz)  / (2 * a)
    print(f"O valor de x' é {xa}")
    print(f"O valor de x'' é {xb}")


