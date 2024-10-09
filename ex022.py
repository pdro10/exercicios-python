#digitar um nome e aparecer na tela com todas as letras maiusculas, minusculas, quantas letras ao todo e
# quantas letras no primeiro nome

nome = str(input("digite seu nome completo: ")).strip()
print(f"seu nome é em maiúsculo é: {nome.upper()}")

print(f"seu nome em minusculo é: {nome.lower()}")

print(len(nome)-nome.count(' '))

print(f"seu primeiro nome tem: {nome.find(' ')}")






