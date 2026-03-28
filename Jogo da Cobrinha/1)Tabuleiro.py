#Essa função deve receber um inteiro n e retornar uma matriz n x n (isto é, uma lista de listas) preenchida apenas com o caractere ".".
#Cada linha do tabuleiro deve ser uma lista.
#O tabuleiro final deve ser uma lista contendo n linhas.
#Todas as posições devem ter o caractere "."

def gera_tabuleiro(n):
    tabuleiro=[]
    elemento=[]
    for i in range(1,n,1):
        elemento.append(".")
    for i in range(1,n,1):
        tabuleiro.append(".")
    return tabuleiro
