#Escreva uma função que recebe uma lista de nomes de alunos e devolve uma lista contendo somente os alunos nos índices ímpares, dividindo a turma em dois.

def alunos_impares(nomes):
    i=1
    lista=[]
    while i<len(nomes):
        lista.append(nomes[i])
        i+=2 
    return lista
