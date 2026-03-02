#Escreva uma função que recebe um número inteiro representando a idade de uma pessoa e devolve uma string conforme a seguinte regra: 
#"crianca" se a pessoa tem até 11 anos, inclusive; "adolescente" se a pessoa tem entre 12 e 17 anos, inclusive; "adulto" se a pessoa tem 18 anos ou mais.

def classifica_idade(idade):
    if idade <=11:
        return "crianca"
    if 11<idade<=17:
        return "adolescente"
    if 17<idade:
        return "adulto"
