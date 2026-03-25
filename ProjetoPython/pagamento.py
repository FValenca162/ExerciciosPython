Vendedor = int(input(" Insira o código do vendedor: "))
CodPeca = int(input(" Insira o código da peça: "))
QuantPeca = int(input("Insira a quantidade de peças: "))
ValorPeca = float(input("Insira o valor da peça: "))

Total = ValorPeca*QuantPeca
Comissao = (Total*5)/100

print (" A comissão do vendedor", Vendedor, " foi de ", Comissao, "  na venda de: ", QuantPeca, "peças, de código: ",CodPeca)
