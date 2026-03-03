#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
#O valor da prestação mensal não pode ser superior a 30% do salário. 
#Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. 

valor_casa=float(input("Valor da casa:"))
salario=float(input("Salário:"))
anos=float(input("Anos a pagar:"))
if valor_casa/(12*anos)<=0.3*salario:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")
