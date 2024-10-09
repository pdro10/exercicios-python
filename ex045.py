# pedra, papel ou tesoura

from random import randint
print("-"*50)
print("jogo do pedra, papel e tesoura")
print("-"*50)
print("""escolha entre:
1 - papel
2 - pedra
3 - tesoura    """)

1 == "papel"
2 == "pedra"
3 == "tesoura"

usuario = int(input("digite o número da sua escolha sua escolha: "))
bot = randint(1, 3)
if usuario == 1:
    if bot == 1:
        resultado = "você escolheu papel e o bot escolheu papel, empate!"
    elif bot == 2:
        resultado = "você escolheu papel e o bot escolheu pedra, você ganhou!"
    elif bot == 3:
        resultado = "você escolheu papel e o bot escolheu tesoura, você perdeu!"
elif usuario == 2:
    if bot == 1:
        resultado = "você escolheu pedra e o bot escolheu papel, você perdeu!"
    elif bot == 2:
        resultado = "você escolheu pedra e o bot escolheu pedra, empate!"
    elif bot == 3:
        resultado ="você escolheu pedra e o bot escolheu tesoura, você venceu!"
elif usuario == 3:
    if bot == 1:
        resultado = "você escolheu tesoura e o bot escolheu papel, você ganhou!"
    elif bot == 2:
        resultado = "você escolheu tesoura e o bot escolheu pedra, você perdeu!"
    elif bot == 3:
        resultado = "você escolheu tesoura e o bot escolheu tesoura, empate!"

print(f"{resultado}")