compra = float(input("Digite o valor da compra: "))
vdesconto = float(input("Digite o valor do desconto: "))/100



valorDesc = compra * vdesconto
Valorfinal = compra - valorDesc

print(f"O valor do desconto é de: {valorDesc} e o valor final a ser pago é de: {Valorfinal}")