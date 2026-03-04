#Faça uma função que recebe os lados de um triângulo e retorna se ele é equilátero, isósceles ou escaleno. 
#Sua função deve retornar a string "equilátero", "isósceles", ou "escaleno". Assuma que os lados do triângulo são válidos.]

def classifica_triangulo(a,b,c):
    if a==b==c:
        return "equilátero"
    if a!=b and a!=c and b!=c:
        return "escaleno"
    else:
        return "isósceles"
