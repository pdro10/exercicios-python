#digite a largura e a altura de uma parede, e saiba a área e quantos L de tinta será necessário para pintar ela


largura = float(input("digite a largura da parede: "))
altura = float(input("digite a altura da parede: "))

area = largura * altura
tintaNece = area / 2

print(f"a parede tem dimensão de {largura}X{altura} e sua área é de {area}m²")
print(f"para pintar essa parede, você precisará de {tintaNece}L de tinta. ")