def voto(nasc):
    obrigatorio = 18
    p = 2024 - saber
    if p >= obrigatorio and p <= 65:
        print(f"vocé tem {p} anos e é obrigado a votar!")
    elif p < obrigatorio:
        print(f"você tem {p} anos e não precisa votar!")
    elif p > 65 and p < 124:
        print(f"você tem {p} anos e seu voto é opcional!")
    else:
        print("digite uma idade válida!")
        return p
    
saber = int(input("digite o ano de nascimento: "))
voto(saber)