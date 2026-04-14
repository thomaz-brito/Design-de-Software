#Você foi contratado para desenvolver uma parte de um software de tradução. 
#Desenvolva uma função que recebe uma lista de palavras em inglês e um dicionário cujas chaves são palavras em inglês e os valores são suas respectivas traduções em português. 
#Sua função deve retornar uma lista das palavras traduzidas para português.

def traduz(palavras,traducao):
    traduzido=[]
    for k in palavras:
        traduzido.append(traducao[k])
    return traduzido 
