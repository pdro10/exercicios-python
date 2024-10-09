c1 = float(input("digite o valor do primeiro comprimento: "))
c2 = float(input("digite o valor do segundo comprimento: "))
c3 = float(input("digite o valor do terceiro comprimento: "))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c2 + c1:
    print("pode formar um triângulo")
    if c1 == c2 == c3:
        print("o seu triângulo é equilátero! ")
    if c1 == c2 != c3 or c1 == c3 != c2 or c2 == c3 != c1:
        print("o seu triângulo é isóceles! ")
    if c1 != c2 and c1 != c3 and c2 != c3:
        print("o seu triângulo é escaleno")
else:
    print("não é possível formar um triangulo")