#Operadores matemáticos
import math

# + <- Soma: soma o valor da esquerda com o da direita
# - <- Subtração: Subtrai o valor da esquerda pelo da direita
# * <- Multiplicação: Multiplica o valor da esquerda com o da direita
# / <- Divisão: Divide o valor da esquerda pelo da direita

# ** <- PotÊncia: Eleva o valor da esquerda pelo da direita
# Math.sqrt(valor) <- Raiz quadrada: Tira a raiz quadrada do valor

# // <- Inteiro da divisão: Quando faz uma divisão que resulta em
# valor float, retorna só a parte inyteira. 10.56 retornaria apenas 10

# % <- Resto da divisão: Retorna o valor de resto quando a divisão
# não é exata. 5/2 teria o resto 1. Útil na identificação de valores par

valor_1= int(input("digite o valor 1: "))
valor_2= int(input("digite o valor 2: "))

print("os valores digitados são ",valor_1," e ",valor_2)

resultado = valor_1 + valor_2
print("A soma dos dois valores é",resultado)

resultado = valor_1 - valor_2
print("A subtração dos dois valores é ",resultado)

resultado = valor_1 * valor_2
print("A multiplicação dos valores é",resultado)

resultado = valor_1 / valor_2
print("A divisão da dos dois valores é",resultado)

resultado = valor_1 ** valor_2
print("O resultado da potenciação dos valores é", resultado)

resultado = valor_1 // valor_2
print("O resultado inteiro dos dois valores é",resultado)

resultado = valor_1 % valor_2
print("O resto de divisão dos valores é", resultado)

resultado = math.sqrt(valor_1)
print("A raiz quadrada de", valor_1,"é",resultado)

print("O valor de pi é", math.pi)
