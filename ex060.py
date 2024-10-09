#ler número e mostrar o fatorial

f = 1
n = int(input("digite um número: "))
c = n
while c > 0:
    print(f"{c} ", end="")
    print("x " if c > 1 else "=", end="")
    f *= c
    c -= 1



print(f"o fatorial de {c} é: {f}")