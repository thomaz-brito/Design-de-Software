#As posições com índices ímpares da lista, devem conter strings com os seguintes operadores "+", "-", "*", "/", "**", "//", "%". Caso exista alguma string diferente das operações listadas acima, então a lista está inválida.
#O último elemento da lista deve ser o operador = ;
#Não é necessário validar as posições pares;
#A lista deve ter no mínimo dois valores;
#Desta forma, implemente uma função chamada valida_entradas que recebe uma lista com as entradas de usuários, como o exemplo acima, e retorna True caso a lista represente entradas de usuário válidas, ou False, caso contrário.

def valida_entradas(lista):
    if len(lista)<2:
        return False
    if lista[len(lista)-1]!= "=":
        return False
    else: 
        for i in range(1,len(lista)-1,2):
            if lista[i] not in ("+","-","*","/","**","//","%"):
                return False
        return True
