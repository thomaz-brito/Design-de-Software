#Faça uma função que recebe um inteiro n e retorna o maior inteiro primo menor ou igual a n. Caso não haja nenhum inteiro primo que se encaixe nessa situação (ex: números negativos), devolva -1.

def maior_primo_menor_que(n):
    if n<2:
        return -1
    elif n==2:
        return n
    else: 
        i=n
        while i>=3:
            a=2
            while a<i:
                if i%a==0:
                    a=i+1
                else:
                    a+=1
                    if a==i:
                        return i
            i-=1
