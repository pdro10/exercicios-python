distancia = float(input("digite a distancia em Kms: "))
if distancia <= 200:
    passagem = distancia * 0.50
    print(f"o valor da passagem é: {passagem}")
else:
    passagem = distancia * 0.45
    print(f"o valor da passagem é: {passagem}")
