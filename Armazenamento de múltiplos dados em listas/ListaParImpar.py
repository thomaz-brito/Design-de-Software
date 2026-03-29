#Faça uma função que recebe uma lista de números e retorna a string 'ímpar', 'par' ou 'misturado' se ela tiver, respectivamente, só números ímpares, só números pares, ou números dos dois tipos. 
#Se a lista for vazia ela deve retornar 'misturado'.

def verifica_lista(l):
    if len(l)==0:
        return "misturado"
    else:
        s=0
        for k in l:
            if k%2==0:
                s+=1
            else:
                s-=1
        if s==len(l):
            return "par"
        if s==-len(l):
            return "ímpar"
        else:
            return "misturado"
