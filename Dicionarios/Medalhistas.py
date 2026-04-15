#Nos jogos olímpicos os esportistas são organizados em uma lista de dicionários. 
#Nesse dicionário existe os campos: nome, nacionalidade, ouro, prata, bronze. 
#Nome e nacionalidade são strings e ouro, prata e bronze são valores numéricos inteiros com a quantidade de medalhas que o esportista ganhou.
#Faça uma função que varre essa lista de dicionários e retorna a nacionalidade que possui mais medalhas de ouro.

def mais_medalhas(lista):
    medalhas={}
    for k in lista:
        if k["nacionalidade"] not in medalhas:
            medalhas[k["nacionalidade"]]=0
        medalhas[k["nacionalidade"]]+=(k["ouro"])
    maior=0
    pais=""
    for x,y in medalhas.items():
        if y>maior:
            maior=y
            pais=x
    return pais
