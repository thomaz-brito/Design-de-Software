#Faça uma função que recebe duas listas, uma de nomes e outra com os respectivos sobrenomes, e devolve uma nova lista com os nomes e os sobrenomes em uma única string. 
#Coloque exatamente um espaço entre o nome e o sobrenome!

def nomes_completos(nome,sobrenome):
    i=0
    nome_completo=[]
    while i<len(nome):
        nome_completo.append(nome[i]+" "+sobrenome[i])
        i+=1
    return nome_completo
