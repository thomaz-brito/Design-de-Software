#Escreva um programa que pergunta a idade da pessoa e diz se a pessoa tem autorização para votar nas eleições brasileiras. 
#Em caso positivo, deve imprimir "Pode votar!". Caso contrário, deve imprimir "Espere um pouco!".

idade=int(input("Digite a sua idade:"))
if idade>=16:
    print("Pode votar!")
else:
    print("Espere um pouco!")
