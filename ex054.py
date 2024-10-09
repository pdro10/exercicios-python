menor = 0
adulto = 0
for i in range(0,7):
    idade = int(input("digite uma idade: "))
    if idade >= 18:
        adulto += 1
    elif idade < 18:
        menor += 1
print(f"temos {menor} menor(es) de idade e {adulto} adulto(s)!")