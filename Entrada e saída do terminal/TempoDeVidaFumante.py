#Escreva um programa que calcule a redução de tempo de vida de um fumante a partir do número de cigarros.
#Pergunte quantos cigarros ele fuma por dia e há quantos anos fuma e imprima o tempo de vida perdido em dias.
#Considere que um cigarro rouba 10 minutos de expectativa de vida.

tempo_perdido=1/(60*24) * 10 * float(input("Quantos cigarros você fuma por dia?")) * 365 * float(input("Há quantos anos você fuma?"))
print (tempo_perdido)
