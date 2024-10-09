preco_normal = float(input(("digite o valor do produto: ")))
condicao = str(input("""escreva a condição de pagamento desejada:
1 = a vista dinheiro/cheque
2 = a vista cartão
3 = em até 2x no cartão
4 = 3x ou mais no cartão: """))

if condicao == "1":
    desconto = preco_normal - (preco_normal * 0.10)
    print(f"com o desconto de 10% o valor do produto será: {desconto}! ")
elif condicao == "2":
    desconto = preco_normal - (preco_normal * 0.05)
    print(f"com o desconto de 5% o valor do produto será: {desconto}! ")
elif condicao == "3":
    print(f"o valor do produto é: {preco_normal}! ")
elif condicao == "4":
    aumento = preco_normal + (preco_normal * 0.20)
    print(f"com 20% de juros, o valor do produto será: {aumento}")