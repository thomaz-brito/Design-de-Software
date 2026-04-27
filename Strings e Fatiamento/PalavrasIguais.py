#De acordo com o Novo Acordo Ortográfico da Língua Portuguesa, usa-se o hífen em compostos que têm palavras iguais ou quase iguais, sem elementos de ligação. 
#Faça uma função que recebe uma string e devolve True se ela for composta por duas palavras iguais ou False, caso contrário.]

def palavras_sao_iguais(s):
    if s[0:s.find("-")] == s[s.find("-")+1:]:
        return True
    else:
        return False
