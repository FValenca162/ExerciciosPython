nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 8:
    print("Sua média é: {:.2f}".format(media), "e seu conceito é A.")
elif media >= 5:
    print("Sua média é: {:.2f}".format(media), "e seu conceito é B.")
else:
    print("Sua média é: {:.2f}".format(media), "e seu conceito é C.")