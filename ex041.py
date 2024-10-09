nasc = int(input("digite o ano de nascimento: "))
idade = 2024 - nasc

if idade <= 9:
    print(f"você tem {idade} anos, você é mirim! ")
elif idade > 9 and idade <= 14:
    print(f"você tem {idade} anos, você é infantil! ")
elif idade > 14 and idade <= 19:
    print(f"você tem {idade} anos, você é junior!")
elif idade == 20:
    print(f"você tem {idade}, você é sênior")
elif idade > 20:
    print(f"você é master! ")