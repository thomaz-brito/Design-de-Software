def desenha_tabuleiro(pos,comida,direcao,tamanho):
    tabuleiro=[]
    for i in range(0,tamanho,1):
        tabuleiro.append(["."]*tamanho)
    
    tabuleiro[comida[0]][comida[1]]="*"
    
    for x in pos:
        tabuleiro[x[0]][x[1]]="o"

    if direcao=="C":
        cabeca="^"
    if direcao=="B":
        cabeca="v"
    if direcao=="E":
        cabeca="<"
    if direcao=="D":
        cabeca=">"
    tabuleiro[pos[0][0]][pos[0][1]]=cabeca

    texto=""
    for x in tabuleiro:
        linha=""
        for k in x:
            linha=linha+f"{k} "
        linha=linha[:-1]
        texto=texto+linha+"\n"

    return texto
