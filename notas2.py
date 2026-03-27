nota= 0
i=0
total=0

nota=int(input("Digite uma nota: "))
notamaior=nota
notamenor=nota

while nota!= -1:
    i+=1
    total+=nota
    
    if nota >notamaior:
        notamaior=nota
        
    elif nota < notamenor:
        notamenor=nota
        
    nota=int(input("Digite uma nota: "))
    
if i != 0:
    mediafinal=total/i
        
    print("A média é: ", mediafinal)
    print("A maior nota é: ", notamaior)
    print("A menor nota é: ", notamenor)
    
else:
    print("Nenhuma nota foi inserida")