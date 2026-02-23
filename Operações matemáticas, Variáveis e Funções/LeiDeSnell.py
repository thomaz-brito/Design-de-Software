#Faça uma função que recebe os valores de n1, n2 e theta1 e retorna o valor do theta2. Os valores passados de n1, n2 são adimensionais, já os valores de theta1 e theta2 deverão ser recebidos e retornados em graus.
import math
def snell_descartes(n1,n2,theta1):
    theta2 = math.degrees(math.asin(math.sin(math.radians(theta1))*n1/n2))
    return theta2
