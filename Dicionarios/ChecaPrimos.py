#Faça uma função que recebe uma lista de números e retorna um dicionário no qual as chaves são os números da lista e os valores são booleanos, indicando se aquele número é primo ou não.

def verifica_primos(lista):
    retorno={}
    for k in lista:
        a=0
        if k==2:
            retorno[2]=True
        elif k<3:
            retorno[k]=False
        else:
            for i in range(2,k,1):
                if k%i==0:
                    a+=1
            if a==0:
                retorno[k]=True
            else:
                retorno[k]=False
    return retorno
