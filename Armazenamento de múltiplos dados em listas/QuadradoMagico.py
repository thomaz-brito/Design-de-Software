#Um quadrado mágico consiste em uma matriz quadrada (mesmo número de linhas e colunas), em que os elementos são organizados de modo que a soma de cada linha, coluna ou de cada umas das duas diagonais principais seja sempre a mesma.
#Faça uma função que recebe como argumento uma lista de listas, como a do exemplo, e retorna True se for um quadrado mágico ou False, caso contrário. 
#Você pode assumir que a função sempre receberá uma matriz de números inteiros positivos, de ordem maior ou igual a três.

def quadrado_magico(Q):
    s=0
    s4=0
    s5=0
    a=0
    for x in Q[0]:
        s+=x
    for x in range(0,len(Q),1):
        s2=0
        s3=0
        for k in Q[x]:
            s2+=k
        for k in Q:
            s3+=k[x]
        if s2==s and s3==s:
            a+=1
        s4+=Q[x][x]
        s5+=Q[x][(len(Q))-1-x]
    if s4==s and s5==s:
        a+=1
    if a==(len(Q)+1):
        return True
    else:
        return False
