i=0

while i <= 3:
    email=(input("Insira seu email: "))
    senha=int(input("Insira sua senha: "))
    i += 1
    if email == "user@email.com" and senha == 12345:
      print("Acesso permitido")
      break
    elif i == 3:
      print("Acesso negado")
      break