#Escreva um programa que pergunta o nome do usuário e imprime "Olá, NOME", onde NOME é o nome do usuário. 
#A menos que o nome do usuário seja Chris. Neste caso, imprima "Todo mundo odeia o Chris".

NOME = input()
if NOME=="Chris":
    print("Todo mundo odeia o Chris")
else:
    print(f"Olá, {NOME}")
