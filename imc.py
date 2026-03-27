peso = float(input("Informe seu peso:" ))
altura = float(input("Informe sua altura em metros:" ))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Está abaixo do peso normal")
elif imc < 24.9:
    print("Está no peso normal")
elif imc < 29.9:
    print("Está com excesso de peso")
elif imc < 34.9:
    print("Está com obesidade grau 1")
elif imc < 39.9:
    print("Está com obesidade grau 2")
else:
    print("Está com obesidade grau 3")

print("Seu imc é: {:.2f}".format(imc))