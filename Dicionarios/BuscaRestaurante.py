def busca_restaurantes(restaurantes, categoria, valor):
    lista=[]
    if categoria=="culinaria":
        for k in restaurantes:
            if k[1]==valor:
                lista.append(k[0])
    if categoria=="ambiente":
        for k in restaurantes:
            if k[2]==valor:
                lista.append(k[0])
    if categoria=="preco":
        for k in restaurantes:
            if k[3]<=valor:
                lista.append(k[0])
    return lista
