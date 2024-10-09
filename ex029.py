veloc = int(input("digite a velocidade do carro: "))
if veloc > 80:
    multa = (veloc - 80) * 7
    print(f"você foi multado! e o valor da multa é: {multa}")
