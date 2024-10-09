num = int(input("digite um número: "))
conversao = str(input("qual conversão você quer utilizar? (1-binario, 2-octal, 3-hexadecimal):"))

if conversao == "1":
    print(f" {num} convertido pra binário é: {bin(num)}")

elif conversao == "2":
    print(f"{num} convertido para octal é: {oct(num)}")

elif conversao == "3":
    print(f"{num} convertido para hexadecimal é: {hex(num)}")

else:
    print("não é disponivel uma conversão diferente de 1,2 ou 3, insira uma válida: ")
    conversao = str(input("qual conversão você quer utilizar? (1-binario, 2-octal, 3-heaxadecimal)"))