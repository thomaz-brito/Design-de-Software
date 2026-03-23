#Faça uma função que recebe duas listas com informações de uma nota fiscal e devolve o preço total da nota. 
#A nota fiscal é representada pelas duas listas, uma com preços de produtos e outra com a respectiva quantidade de itens comprados daquele produto.

def calcula_total_da_nota(preco,quantidade):
    soma=0
    for i in range(0,len(preco),1):
        soma=soma+preco[i]*quantidade[i]
    return soma
