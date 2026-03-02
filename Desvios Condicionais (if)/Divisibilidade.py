#Faça uma função que recebe como entrada um número inteiro e testa a divisibilidade por 2 e 3.
#Se for divisível por 2, sua função deve retornar a string "Ins". Se for por 3, retorna "per". Porém, se for por 2 e 3 ao mesmo tempo retorna "Insper". 
#Para outros casos, sua função deve devolver o próprio número.

def divisivel(x):
    if x%2==0 and x%3==0:
        return "Insper"
    if x%2==0:
        return "Ins"
    if x%3==0:
        return "per"
    else:
        return x
