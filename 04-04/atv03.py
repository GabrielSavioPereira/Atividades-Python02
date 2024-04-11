salario = float(input("Digite o salario do funcionario: "))

if salario <= 1000:
    salario_novo = salario * 1.1
    print ("O salario de quem recebe até R$ 1000 é de: ",salario_novo)
else:
    salario_novo = salario * 1.05
    print("O salario de quem recebe mais de R$ 1000 é de: ",salario_novo)   