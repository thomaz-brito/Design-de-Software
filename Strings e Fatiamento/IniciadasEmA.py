#Faça um programa que pergunte ao usuário palavras e preencha uma lista. O programa deve parar com a palavra "fim". 
#Ao final, imprima somente as palavras em que a primeira letra seja "a". Use um print por palavra.

while True:
    palavra=input("")
    if palavra=="fim":
        break
    if palavra[0]=="a":
        print(palavra)
