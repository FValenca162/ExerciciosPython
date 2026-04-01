i=0
nome=""
maioridade=0
idade=0

while True:
    nome=(input("Insira o seu nome:"))
    
    if nome == "encerrar":
        break
     
    idade=int(input("Insira a sua idade:"))
    print("digite 'encerrar' para parar")
    i+=1
    
    if idade>=18:
        maioridade=maioridade+1
   

print(f"{i} usuários forma cadastrados e {maioridade} usuários são maiores de idade")
    
    