num = int(input("digite um número: "))
tot = 0
for i in range(1, num + 1):
    if num % i == 0 :
        tot += 1

if tot == 2:
    print(f"o número {num} foi dividido {tot} vezes e por isso ele é primo!")
else:
    print(f"o número {num} foi dividido {tot} vezes e por isso ele não é primo!")


