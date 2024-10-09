p1 = int(input("digite o primeiro termo da PA: "))
r = int(input("digite a razão: "))
dt = p1 + (10 - 1) * r
for i in range(p1, dt + r, r):
    print(i, end="--")