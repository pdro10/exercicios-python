s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        s += c
print(f"a soma de todos os {count} valores digitados é: {s}")
