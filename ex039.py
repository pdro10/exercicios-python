nasc = int(input("digite o ano de nascimento: "))
idade = 2024 - nasc

if idade < 18:
    saldo = 18 - idade
    print(f"você não precisa se alistar ainda! falta {saldo} para se alistar")
elif idade == 18:
    print(f"você tem 18 anos, deve se alistar imediatamente! ")
elif idade > 18:
    tempo = idade - 18
    print(f"você tem {idade}, já deveria ter se alistado há {tempo}")

