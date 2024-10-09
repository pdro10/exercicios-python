saber = str(input("digite o ano: "))
chave = int(input("o Mês de fevereito tem 28 ou 29 dias?"))

if chave == 29:
    print(f"o ano {saber} é bissexto!")
else:
    print(f"o ano {saber} não é bissexto! ")