preco = float(input("Qual o preço original [em R$]:"))
desconto = float(input("Qual o desconto [em %]:"))
valor_desconto = preco*desconto/100
valor_final = preco - valor_desconto
print("Preço original", preco)
print("Você ganhou R$", valor_desconto, "de desconto")
print("Valor do produto com o desconto", valor_final)
