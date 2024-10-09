# def contador(*paramentros):
#     for c in range(1, 11, 1):
#         print(c)
#         if c > 10:
#             break
        

# contador()

# def contador2(*paramentros):
#     for c in range(10, -1, -2):
#         print(c)
#         if c < 0:
#             break

# contador2()

def contador3(*parametros):
    i = int(input("digite o número de início da contagem: "))
    f = int(input("digite o número de finalização da contagem: "))
    p = int(input("digite o passo da contagem: "))
    for c in range(i, f, p):
        if f in "-":
            if c < -f:
                break
        else:
            if c > f:
                break
        print(c)


contador3()

