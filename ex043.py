peso = float(input("digite o peso: "))
altura = float(input("digite a altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"seu imc foi {imc:.2f}, você está abaixo do peso! ")
elif imc >= 18.5 and imc < 25:
    print(f" seu imc foi {imc:.2f}, você está no peso ideal! ")
elif imc >= 25 and imc < 30:
    print(f" seu imc foi {imc:.2f}, você está em sobrepeso! ")
elif imc >= 30 and imc <= 30:
    print(f" seu imc foi {imc:.2f}, você está com obesidade ")
elif imc > 40:
    print(f"seu imc foi: {imc:.2f}, você está com obesidade moórbida! ")

