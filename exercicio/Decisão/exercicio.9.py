numero_1 = float(input("Dê o valor de um produto: "))
numero_2 = float(input("Dê outro produto: "))
numero_3 = float(input("Dê outro produto: "))

if numero_1 < numero_2 and numero_1 < numero_3: print( numero_1,"é o mais barato, compre esse")

if numero_2 < numero_1 and numero_2 < numero_3: print( numero_2,"é o mais barato, compre esse")

if numero_3 < numero_2 and numero_3 < numero_1: print( numero_3,"é o mais barato, compre esse")