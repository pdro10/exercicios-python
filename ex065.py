# le varios numeros, mostre a media entre todos os valores, qual o maior e o menor, quer continuar a digitar ou nao
# n = int(input("digite um número:"))
# media = s / q
# maior = 
# menor = 
# print("quer continuar digitando? s/n")
# int(input("quer continuar digitando? s/n"))

soma = 0
quant = 0
media = 0
maior = 0
menor = 0
resp = "s"
while resp in "Ss":
    num = int(input("digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    resp = str(input("quer continuar [S/N]:")).strip().lower()[0]
media = soma / quant
print(f"você digitou {quant} números, e a media foi {media}")
print(f" o maior valor foi: {maior} e o menor foi:{menor}")
