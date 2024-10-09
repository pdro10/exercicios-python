# crie um progrmaa que le varios numeros, vai parar quando digitiar 999, no final mostre quantos digitados 
# e a soma entre eles, sem o 999

# n1 = 0
# while n != 999:
#     n = int(input("digite um número[999 para parar]: "))
#     if n == 999:
#         break
#     if n != 999:
#         n2 += 1
#         n += n
#         print(f"a soma entre os números digitados é {n} e quantidade é {n2}")

num = 0
cont = 0
soma = 0
num = int(input("digite um número[999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("digite um número[999 para parar]: "))
print(f"você digitou {cont} e a soma entre eles foi: {soma}")
