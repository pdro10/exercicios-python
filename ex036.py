casa = float(input("digite o valor da casa: "))
salario = float(input("digite o valor do salario do comprador: "))
anos = int(input("em quantos anos irá ser pago? "))

mensal = casa / (anos * 12)
minimo = salario * 0.30

if mensal <= minimo:
    print("o emprestimo está autorizado ")
else:
    print("o emprestimo está negado ")