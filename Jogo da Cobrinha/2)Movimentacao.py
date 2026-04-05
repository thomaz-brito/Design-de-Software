def movimenta_cobra(pos, direcao, cresce, tam_tabuleiro):
    if direcao=="C":
        if pos[0][0]==0:
            cabeca=[tam_tabuleiro-1,pos[0][1]]
        else:
            cabeca=[pos[0][0]-1, pos[0][1]]
    if direcao=="B":
        if pos[0][0]==tam_tabuleiro-1:
            cabeca=[0, pos[0][1]]
        else:
            cabeca=[pos[0][0]+1, pos[0][1]]
    if direcao=="E":
        if pos[0][1]==0:
            cabeca=[pos[0][0], tam_tabuleiro-1]
        else:
            cabeca=[pos[0][0], pos[0][1]-1]
    if direcao=="D":
        if pos[0][1]==tam_tabuleiro-1:
            cabeca=[pos[0][0], 0]
        else:
            cabeca=[pos[0][0], pos[0][1]+1]

    pos.insert(0,cabeca)

    if cresce == False:
        del pos[len(pos)-1]

    return pos
