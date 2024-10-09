# prog q ler 2 valores, mostre um menu na tela 1  somar, 2 = mult, 3 = maior, 4 = novos numeros, 5 = sair
# progrmama efetuando a operação desejada
# sair = "5"
while True:
    print('''
    [ 1 ] = SOMAR
    [ 2 ] = MULTIPLicAR
    [ 3 ] = MAIOR
    [ 5 ] = SAIR
    ''')
    menu = int(input("digite a operação que você deseja realizar, 5 caso queira sair: "))
    if menu == 5:
        print("voce saiu")
        break
    else:
        if menu == 1:
            v = int(input("digite um valor: "))
            v2 = int(input("digite um segundo valor: "))
            s = v + v2
            print(f"o valor da soma é {s}")
        elif menu == 2:
            v = int(input("digite um valor: "))
            v2 = int(input("digite um segundo valor: "))
            m = v * v2
            print(f"o valor da multiplicação é {m}")
        elif menu == 3:
            v = int(input("digite um valor: "))
            v2 = int(input("digite um segundo valor: "))
            if v2 > v:
                print(f"o valor {v2} é o maior! ")
                print(f"o valor {v} é o menor!")
            if v2 < v:
                print(f"o valor {v} é o maior! ")
                print(f"o valor {v2} é o menor!")
            if v == v2:
                print(f"não há valor maior e nem menor, pois {v} e {v2} são iguais! ")
        else:
            print("inválido")

