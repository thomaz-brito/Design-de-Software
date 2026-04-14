#Faça uma função que recebe dois dicionários e retorna uma lista contendo os valores que estão presentes em ambos os dicionários.

def interseccao_valores(d1,d2):
    interseccao=[]
    for a in d1.values():
        for b in d2.values():
            if a==b:
                interseccao.append(b)
    return interseccao
