import time
escolha=True
while escolha:
    print("\n")
    print("Converter Decimal em Binário e vice-versa")
    print("""
    1. Converter Decimal em Binário
    2. Converter Binário em Decimal
    8.Exit/Quit/Saída
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        numero_decimal = int(input("Digite o número decimal: "))
        binario_numero_converter = bin(numero_decimal)
        print("   Número Decimal        Número Binário   ")
        print(f"         {numero_decimal}                {binario_numero_converter}  ")
        time.sleep(2)
    elif escolha=="2":
        numero_binario = int(input("Digite o número binário: "))
        b = str(numero_binario)  # Converter o valor para uma string
        decimal_value = 0
        power = 0
        for bit in reversed(b):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1
        print("  Número Binário                Número Decimal         ")
        print(f"         {numero_binario}                           {decimal_value}  ")
        time.sleep(2)
    elif escolha=="0":
      print("\n Adeus")
      escolha = None
    else:
       print("\n Escolha não válida.\n Tente outra vez.")