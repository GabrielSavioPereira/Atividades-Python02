import math

raio1 = float(input("Qual o Raio Externo:"))
raio2 = float(input("Qual o Raio Interno:"))
area = math.pi * (raio1**2-raio2**2)
if raio2 >= raio1:
    print("Infelizmente sua área é invalida")
else: 
    print("Área =", area)
