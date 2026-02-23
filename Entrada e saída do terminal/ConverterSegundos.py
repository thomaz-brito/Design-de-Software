#Escreva um programa que pergunte, em sequência, uma quantidade de dias, horas, minutos e segundos para o usuário. Depois calcule o total em segundos e imprima.

segundos_totais=24*60*60*int(input("Número de dias")) + 60*60*int(input("Número de horas")) + 60*int(input("Número de minutos"))+int(input("Número de segundos"))
print(segundos_totais)
