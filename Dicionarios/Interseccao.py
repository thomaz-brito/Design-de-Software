#Faça uma função que recebe dois dicionários e retorna uma lista contendo os valores que estão presentes em ambos os dicionários.

def interseccao_valores(d1,d2):
    interseccao=[]
    for a,b in d1.items():
        for c,d in d2.items():
            if b==d:
                interseccao.append(b)
    return interseccao
