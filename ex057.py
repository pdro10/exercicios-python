#faca um programa que leia o sexo de uma pessoa, so aceita m ou f, se n for pede pra digitar até estar valida
m = "masculino"
f = "feminino"
# # s = str(input("digite o sexo da pessoa M para Masculino, F para Feminino: ")).lower().strip()
s = ""
while s != "m" or s != "f":
    s = str(input("digite o sexo da pessoa M para Masculino, F para Feminino:")).lower().strip()
    if s == "m":
        print(f"o sexo digitado é: {m}")
        break
    if s == "f":
        print(f"o sexo digitado é: {f}")
        break
    if s == "5":
        break



