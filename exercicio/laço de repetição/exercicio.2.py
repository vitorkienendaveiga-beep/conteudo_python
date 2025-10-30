nome = input("Digite o seu nome: ")
while len(nome) < 3:
    print(f"Nome inválido, ele precisa ter mais de 3 caracteres")
    nome = input("Digite o seu nome:")
    
idade = int(input("Digite a sua idade"))
while idade <0 or idade > 150:
    print(f"Idade inválida, ela precisa ser entre 0 e 150")

salario = float(input("Digite o seu salario: "))
while salario < 0:
    print("salario invalido, ele precisa ser maior que 0")

print("S - Solteiro | C - Casado | V - Viuvo | D - Divorciado")
estado_civil = input("Digite seu estao civil: ").lower()
#while estado_civil not in('s','c','v','d'): //Outra opção exclusiva Python
while estado_civil !='S' and estado_civil !='C' and estado_civil !='V' and estado_civil !='D':
    print("Opção inválida, digite de acordo com as opções disponíveis")
    print("S - Solteiro | C - Casado | V - Viuvo | D - Divorciado")
    estado_civil=input("Digte seu estado civil: ").lower()

print(f"Você é",nome,"tem",idade,"anos","seu salario é de", salario, "e seu estado civil é",estado_civil)