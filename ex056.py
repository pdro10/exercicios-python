id = 0
menorM = 0
maiorIdadeHomem = 0
nomeVelho = ""
for p in range(1, 5):
    nome = str(input("digite um nome: ")).strip()
    idade = int(input("digite uma idade: "))
    sexo = str(input("digite o sexo M para masculino e F para feminino: ")).lower().strip()
    id += idade
    if p == 1 and sexo == "m":
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == "m" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == "f":
        if idade < 20:
            menorM += 1

media = id / 4
print(f"A media de idade é: {media}, o homem mais velho é: {nomeVelho} e tem: {maiorIdadeHomem} anos!")
print(f"Há {menorM} mulher(es) com menos de 20 anos!")