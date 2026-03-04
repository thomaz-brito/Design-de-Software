#aca Wars! Você mora no sítio, e está em guerra com seu vizinho. Você dispõe de uma catapulta de lançamento de jacas, onde você consegue escolher a velocidade v e o ângulo , em graus, de lançamento da jaca. Uma jaca quando cai se espalha por um raio de 2 metros. Seu alvo é a catapulta do vizinho, que está à 100 metros da sua.
#Faça um programa que pede a velocidade e o ângulo de lançamento da sua jaca, e diz se ela cairá muito perto, muito longe, ou acertará o alvo. Considere que a jaca acerta o alvo se cai à uma distância do alvo menor que o seu raio de espalhamento. 
#Os possíveis valores impressos são 'Muito perto', 'Muito longe' e 'Acertou!'. Considere "Muito perto" se não chegou no alvo, e "Muito longe" se passou do alvo.

import math as m
v=float(input())
a=float(input())
d=v**2*m.sin(m.radians(2*a))/9.8
if d<98:
    print("Muito perto")
if 98<=d<=102:
    print("Acertou!")
if d>102:
    print("Muito longe")
