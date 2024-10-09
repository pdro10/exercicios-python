n1 = float(input("digite uma nota: "))
n2 = float(input("digite outra nota: "))
media = (n1 + n2) / 2

if media >= 0 and media < 5.0:
    print(f"sua média foi {media}, você foi reprovado!")
elif media >=5 and media < 7:
    print(f"sua média foi {media}, você está de recuperação")
elif media >= 7 and media <=10:
    print(f"sua média foi {media}, você foi aprovado")
else:
    print("não há como atingir essa média")