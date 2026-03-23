#Implemente uma função que recebe uma grade horária, um número entre 0 e 4 representando o dia da semana (0 é segunda-feira e 4 é sexta-feira) e um número entre 0 e 3 representando um período do dia e devolve o nome do compromisso marcado para esse período. 
#Se não houver compromisso nesse período (representado por uma string vazia), sua função deve devolver 'Livre'.
#A grade horária é representada por uma lista de listas como a lista a seguir (atenção, esse é apenas um exemplo - a grade horária deve ser recebida como argumento da sua função e será diferente deste exemplo, mas possuirá a mesma quantidade de elementos):

def compromisso_no_periodo(grade,n1,n2):
    if grade[n2][n1]=="":
        return "Livre"
    else:
        return grade[n2][n1]
