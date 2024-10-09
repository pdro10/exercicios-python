salario = float(input("digite o valor do salário: "))
if salario > 1250:
    aumento = salario + salario * 0.10
else:
    aumento = salario + salario * 0.15

print(f"o seu novo salario é: {aumento}")