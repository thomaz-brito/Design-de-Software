#Escreva um programa que pergunta para o usuário o valor da conta do restaurante e imprime: "Valor da conta com 10%: R$ X.YZ", onde X.YZ é o valor da conta mais os 10% com exatamente duas casas decimais.
valor_bruto=float(input("valor bruto da conta"))
conta=1.1*valor_bruto
print(f"Valor da conta com 10%: R$ {conta:.2f}")
