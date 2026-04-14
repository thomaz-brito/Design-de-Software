#Uma loja de livros usa uma tabela de cores para identificar o preço em Reais de cada livro. O seu catálogo de livros está armazenado em um dicionário que indica a cor da tabela de preços de cada livro. 
#A tabela de conversão de cor para preço está armazenada em um dicionário que indica o preço da tabela de preços para cada cor.
#Faça um função que receba uma string com o título de livro, um dicionário com os nome dos livros indicando a cor da tabela de preços e um dicionário das cores para os preços e retorne o preço de um livro em Reais a partir de seu nome.
#Sua função deve se chamar verifica_preco.

def verifica_preco(titulo,catalogo,precos):
    return precos[catalogo[titulo]]
