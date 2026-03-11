#Bhāskara foi um matemático indiano do século VII que desenvolveu uma fórmula simples para calcular o valor do seno aproximado de um número em graus.
#Desenvolva um programa que imprima o ponto de maior erro da função de Bhāskara.
#Para isso, teste os valores de 0 a 90 graus, de um e um grau, analise a diferença da função de Bhāskara em relação a função math.sin do Python e diga qual é o valor em graus que o valor de seno apresenta a maior diferença entre ambas as técnicas.


import math as m
x=0
maior=0
while x<=90:
    bask=4*x*(180-x)/(40500-x*(180-x))
    dif=abs(m.sin(m.radians(x))-bask)
    if dif>maior:
        maior = dif
        arco=x
    x+=1
print(arco)
