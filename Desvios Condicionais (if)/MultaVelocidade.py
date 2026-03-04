#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80km/h, o usuário deverá ser multado. Nesse caso exiba uma mensagem com o valor da multa, cobrando R$5,00 por km acima de 80.


velocidade=int(input("Qual a velocidade?"))
if velocidade>80:
    multa=5*(velocidade-80)
    print(f"{multa: .2f}")
else: 
    print("Não foi multado")
