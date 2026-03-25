nome = str(input("Insira seu nome:"))
salariobase = float(input("Insira seu salario atual:"))

if 0 < salariobase < 1000:
    novosalario= salariobase+(20*salariobase)/100
    
elif 1000.1 < salariobase <5000:
    novosalario= salariobase+(10*salariobase)/100
    
else:
    novosalario= salariobase+(5*salariobase)/100

print("O novo salario do jogador: " , nome, " é de: ", novosalario)