#digite a quantidade de dias alugados e os Kms rodados e receba o valor a ser pago 
dias = int(input("digite quantos dias alugados: "))
km = float(input("digite quantos Km rodados: "))

preco = (60 * dias) + (0.15 * km)

print(f"com {dias} alugados e {km}km rodados, o preço a pagar será: {preco}!")