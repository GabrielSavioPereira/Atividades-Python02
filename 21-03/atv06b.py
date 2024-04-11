litros = float (input("Digite a quantidade de combustivel abastecido: "))
combust = input("Digite A para alcool e G para gasolina: ").upper()

if combust == "G":
    ValorGasolina = 5.57
    if litros <=20:
        ValorTot = ValorGasolina * litros
        desc = 4/100
        ValorDesc = ValorTot * desc
        ValorFinal = ValorDesc - ValorTot
        print(f"O valor com menos de 20 litros de Alcool é de {ValorDesc}")

elif litros >20:
     ValorTot = ValorGasolina * litros
     desc = 6/100
     ValorDesc = ValorTot * desc
     ValorFinal = ValorDesc - ValorTot
     print(f"O valor com mais de 20 litros de Alcool é de {ValorDesc}")

if combust =="A":
    ValorAlcool = 4.98
    if litros <=20:
        Vtotal = ValorAlcool * litros
        desc = 2/100
        Valordescontado = Vtotal * desc 
        ValorFim = Vtotal - Valordescontado
        print(f"O valor com menos de 20 litros de Alcool é de {ValorFim}")
elif litros >20:
    Vtotal = ValorAlcool * litros
    desc = 2/100
    Valordescontado = Vtotal * desc 
    ValorFim = Vtotal - Valordescontado
    print(f"O valor com mais de 20 litros de Alcool é de {ValorFim}")