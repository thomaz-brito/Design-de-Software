#As boias fabricadas têm sempre o formato de um toróide (torus), que é definido pelo raio interno da boia (R) e o raio da seção transversal dela (r). 
#As boias possuem um peso (P) medido por uma balança.
#Sua função é descobrir se a boia vai "boiar" ou não. Considere que a densidade da água para a temperatura ambiente é de 997 kg/m³ ou 0,997 g/cm³ e qualquer coisa com densidade menor ou igual a esse valor irá boiar.
#Lembre-se que a densidade é calculada como o peso dividido pelo volume.

import math as m
def vai_boiar(P,R,r):
    if P/(2*m.pi**2*R*r**2*0.01**3)<=997:
        return(True)
    else:
        return(False)
