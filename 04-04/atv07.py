vmaxima = float (input("Digite a velocidade maxima na via: "))
vmotorista =float( input("Qual a velocidade em que o carro estava: "))  

if vmotorista  >= vmaxima+10 and vmotorista < vmaxima +11:
    multa = 85.13
    pontos = 3
    print(f"O motorista passou a {vmotorista} e suas consequencias foram -{pontos} na carteira e R$ {multa}")
elif vmotorista >= vmaxima +11 and vmotorista <= vmaxima +30:
    multa2 =127.69
    pontos2 = 5
    print(f"O motorista passou a {vmotorista} e suas consequencias foram -{pontos2} na carteira e R$ {multa2}")
elif vmotorista  >= vmaxima+31:
    multa3 =574.62
    pontos3 = 7
    print(f"O motorista passou a {vmotorista} e suas consequencias foram -{pontos3} na carteira e R$ {multa3}")