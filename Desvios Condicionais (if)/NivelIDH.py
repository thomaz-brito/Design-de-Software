#Faça uma função que recebe um valor de IDH e retorna o seu respectivo nível.

def nivel_idh(IDH):
    if 0.800<=IDH<=1.000:
        return "Muito Alto"
    if 0.700<=IDH<0.800:
        return "Alto"
    if 0.555<=IDH<0.700:
        return "Médio"
    if 0.350<=IDH<0.555:
        return "Baixo"
    if IDH<0.350:
        return "Sem dados"
