#Faça uma função que recebe como entrada a data de nascimento de uma pessoa e uma outra data (posterior ao nascimento) 
#e retorna a idade da pessoa na última data passada (retorna o valor da idade como um número inteiro). 
#A função deve receber 6 argumentos: dia, mês e ano de nascimento, e dia, mês e ano da data posterior.

def calcula_idade(d1,m1,a1,d2,m2,a2):
    if m2>m1 or (m1==m2 and d2>=d1):
        idade=a2-a1
    else:
        idade=a2-a1-1
    return idade 
