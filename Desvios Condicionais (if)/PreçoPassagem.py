#Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km. 
#Seu programa deve imprimir o preço da passagem, cobrando 50 centavos por quilômetro para viagens de até 200km e 45 centavos por quilômetro extra para viagens mais longas.

distancia = float(input("Distância que deseja percorrer:"))
if distancia <= 200:
    print(f"{0.5*distancia:.2f}")
else:
    print(f"{200*0.5+(distancia-200)*0.45:.2f}")
