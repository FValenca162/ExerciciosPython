def funcaototal(p,q):
    total= p*q
    return total

preco=float(input("Insira o valor do produto: "))
quantidade=float(input("Insira a quantidade de produtos: "))

resultado=funcaototal(preco,quantidade)
print("O valor total a pagar é: ", resultado)