#Faça uma função que calcula a posição de um corpo em movimento retilíneo uniformemente variado. Onde s_0 é a posição inicial, v_0 é a velocidade inicial, a é a aceleração linear e t é o tempo decorrido. A função deve receber os argumentos na ordem: posição inicial, velocidade inicial, aceleração e tempo decorrido.

def calcula_posicao(s_0,v_0,a,t):
    posicao=s_0+v_0*t+a*t**2/2
    return posicao
