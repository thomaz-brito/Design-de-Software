def cobra_vai_comer(pos,comida,direcao):
    if direcao=="C":
        cabeca=[pos[0][0]-1, pos[0][1]]
    if direcao=="B":
        cabeca=[pos[0][0]+1, pos[0][1]]
    if direcao=="E":
        cabeca=[pos[0][0], pos[0][1]-1]
    if direcao=="D":
        cabeca=[pos[0][0], pos[0][1]+1]

    if cabeca==comida:
        return True
    else:
        return False
