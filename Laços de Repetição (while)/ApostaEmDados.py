#Um determinado Cassino em Las Vegas precisa de um sistema para simular a contabilização de ganhos e perdas num determinado jogo de dados. 
#O jogo consiste em adivinhar qual das seis faces de um dado irá ficar com a face para cima após o dado ser lançado de forma aleatória sobre uma mesa.
#Você deve implementar uma função que simula os ganhos e perdas desse jogo. O jogo funciona da seguinte maneira: o jogador escolhe um número da sorte, um valor para aposta e o número de rodadas que irá simular, passando então esses valores, nessa ordem, como parâmetros para a função de simulação que você vai criar.
#A cada rodada um número é sorteado, entre 1 e 6. Se o número da sorte for igual ao número sorteado, então, o valor da aposta é aumentado em 1/3; caso contrário, se os números forem diferentes, então o valor da aposta é decrescido em 1/6. O valor inicial da aposta da próxima rodada é o valor resultante da rodada anterior, sendo o número total de rodadas é dada pelo usuário.
#Ao final de todas as rodadas, a função deve retornar o valor total do apostador após os ganhos e perdas de todas as rodadas.
#Nota: o usuário irá escolher apenas valores inteiros para o número da sorte escolhido e para o número de rodadas, porém, pode escolher números com decimais para o valor inicial da aposta. O retorno da função é um número com casas decimais.


import random as r
def apostando_em_dados(n,aposta,rodadas):
    i=0
    while i<rodadas:
        i+=1
        sorteado=r.randint(1,6)
        if sorteado==n:
            aposta=aposta*4/3
        else:
            aposta=aposta*5/6
    return aposta
