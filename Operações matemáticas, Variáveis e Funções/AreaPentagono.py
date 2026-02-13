#faça uma função que recebe a medida de um dos lados l do pentágono e calcula sua área total.

import math
def calcula_area_do_pentagono(l):
    area=5*l**2/(4*math.tan(math.pi/5))
    return area
