#Escreva uma função que recebe um número, representando um ano, e retorna True se o ano é bissexto e False caso contrário.

def eh_bissexto(ano):
    if (ano/4)%1==0:
        if (ano/100)%1==0:
            if (ano/400)%1==0:
                return(True)
            else:
                return(False)
        else:
            return(True)
    else:
        return(False)
