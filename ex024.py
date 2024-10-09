#saber se a cidade digitada começa com nome de "santo"

cidade = str(input("digite o nome de uma cidade: ")).strip()
print(cidade[0:5].lower() == "santo")
