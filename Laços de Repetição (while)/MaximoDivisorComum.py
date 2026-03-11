#Faça uma função para encontrar o máximo divisor comum entre dois números

def maximo_divisor_comum(x,y):
    k=1
    while k<=x and k<=y:
        if x%k==0 and y%k==0:
            mdc=k
        k+=1
    return mdc
