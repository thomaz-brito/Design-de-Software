#Em processamento de dados, sempre são necessárias limpeza e uniformização dos dados. Um grande problema sempre são datas, que podem vir em diversos formatos.
# Faça uma função que recebe um texto com uma data e um texto com seu formato e devolva a data formatada no padrão aaaa-mm-dd.

def formata_data(data, modelo):
    retorno = ""
    sep = modelo[1]

    modelo = modelo.replace(sep,"")
    pa = modelo.find("a")
    pm = modelo.find("m")
    pd = modelo.find("d")

    lista = data.split(sep)
    if len(lista[pa]) == 2:
        lista[pa] = str(int(lista[pa]) + 2000)
    if len(lista[pd]) == 1: 
        lista[pd] = "0" + lista[pd] 
    for elemento in [pa,pm,pd]:
        retorno += lista[elemento]
        retorno += "-" 
    
    retorno = retorno[:len(retorno)-1]

    return retorno
