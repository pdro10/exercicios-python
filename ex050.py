s = 0
for i in range(0,7):
    n = int(input("digite o número: "))
    if n % 2 == 0:
        s += n
        # print(f"a soma está em {s}") caso queira que apareça quanto está a soma enquanto digita
print(f"o resultado final foi {s}")
