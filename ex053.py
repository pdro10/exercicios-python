frase = str(input("digite uma frase: ")).strip().lower()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for i in range(len(junto) - 1,-1, -1):
    inverso += junto[i]
if inverso == junto:
        print("é um palindromo! ")
else:
        print("não é um palindromo! ")














# if palavra == palindromo:
#     print(" é um palindromo")
# else:
#     print("não é um palindromo")