n1 = int(input("digite um número: "))
n2 = int(input("digite o segundo número: "))
n3 = int(input("digite o terceiro número: "))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3


print(f"o maior é: {maior} e o menor é {menor}")
