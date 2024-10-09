from random import randint
jogador = ""
comp = randint(0,10)
palpite = 0
while jogador != comp:
    jogador = int(input("digite um número entre 0 e 10: "))
    comp = randint(0, 10)
    if jogador != comp:
        print(f"comp escolheu {comp} e você {jogador}, você errou!")
        palpite += 1
    if jogador == comp:
        print(f"o comp escolheu {comp} e você {jogador}, você acertou!")
        print(f"você acertou em {palpite} palpites!")
