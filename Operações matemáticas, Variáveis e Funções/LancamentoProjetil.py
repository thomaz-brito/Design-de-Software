# Faça uma função que calcule a distância alcançada por um projétil lançado com velocidade v em um ângulo theta, de uma altura y0.
import math
g=9.8
def calcula_distancia_do_projetil(v,theta,y0):
    d=v**2/(2*g) * (1+math.sqrt(1+2*g*y0/(v*math.sin(theta))**2))*math.sin(2*theta)
    return d 
