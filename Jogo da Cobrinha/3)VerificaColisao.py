def verifica_colisao(corpo):
    i=0
    for x in corpo:
        if corpo[0]==x:
            i+=1
    if i>=2:
        return True
    else:
        return False
