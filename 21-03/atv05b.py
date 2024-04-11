n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3)/3;

if media >=7:
    print("Parabéns! Sua média é alta.")
elif media ==5:
    print("Sua média é razoável.")
else:
    print("Sua média é baixa. É uma boa oportunidade para melhorar")