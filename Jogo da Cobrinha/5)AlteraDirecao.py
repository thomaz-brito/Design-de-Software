def altera_direcao(atual,novo):
    if (atual=="C" and novo=="B") or (atual=="B" and novo=="C") or (atual=="E" and novo=="D") or (atual=="D" and novo=="E"):
        return atual
    else:
        return novo
