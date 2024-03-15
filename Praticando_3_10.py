import math

diametro = float(input("Qual o Diâmetro interno [m]:"))
fluxo = float(input("Qual o fluxo [m/s]"))
vazao = math.pi*((diametro/2)**2)*fluxo
print("Vazão =", vazao)
