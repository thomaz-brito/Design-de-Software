#Faça uma função que recebe 4 números, x1, y1, x2, y2, e retorna a distância entre os pontos (x1,y1) e (x2,y2).

def distancia_euclidiana(x1,y1,x2,y2):
    distancia=((x1-x2)**2+(y1-y2)**2)**0.5
    return distancia
