import math

raio = float(input("Qual o raio:"))
altura = raio * math.cos(math.radians(30))
area = 6 * (raio*altura)/2
print("Área =", area)


