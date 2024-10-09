# digite o valor de um produto e descubra o novo preço dele após receber desconto de 5%

preco = float(input("digite o preço do produto: "))
desconto = preco * 0.05
n_preco = preco - desconto

print(f"com o desconto de 5%, o valor da compra ficou em {n_preco} ")