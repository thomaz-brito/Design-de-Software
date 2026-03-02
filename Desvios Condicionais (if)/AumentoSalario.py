#Escreva uma função que recebe o salário atual do funcionário e calcule o valor do aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15% (Adaptado do ex. 4.4 livro Nilo Ney).

def calcula_aumento(salario):
    if salario > 1250:
        return 0.1*salario
    else: 
        return 0.15*salario
