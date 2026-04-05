def desenha_tabuleiro(pos,comida,direcao,tamanho):
    tabuleiro=[]
    for i in range(0,tamanho,1):
        tabuleiro.append(["."]*tamanho)
    
    tabuleiro[comida[0]][comida[1]]="*"
    
    for x in pos:
        tabuleiro[x[0]][x[1]]="o"

    if direcao=="C":
        cabeca="^"
    if direcao=="B":
        cabeca="v"
    if direcao=="E":
        cabeca="<"
    if direcao=="D":
        cabeca=">"
    tabuleiro[pos[0][0]][pos[0][1]]=cabeca

    texto=""
    for x in tabuleiro:
        linha=""
        for k in x:
            linha=linha+f"{k} "
        linha=linha[:-1]
        texto=texto+linha+"\n"
    return texto

def movimenta_cobra(pos, direcao, cresce, tam_tabuleiro):
    if direcao=="C":
        if pos[0][0]==0:
            cabeca=[tam_tabuleiro-1,pos[0][1]]
        else:
            cabeca=[pos[0][0]-1, pos[0][1]]
    if direcao=="B":
        if pos[0][0]==tam_tabuleiro-1:
            cabeca=[0, pos[0][1]]
        else:
            cabeca=[pos[0][0]+1, pos[0][1]]
    if direcao=="E":
        if pos[0][1]==0:
            cabeca=[pos[0][0], tam_tabuleiro-1]
        else:
            cabeca=[pos[0][0], pos[0][1]-1]
    if direcao=="D":
        if pos[0][1]==tam_tabuleiro-1:
            cabeca=[pos[0][0], 0]
        else:
            cabeca=[pos[0][0], pos[0][1]+1]

    pos.insert(0,cabeca)

    if cresce == False:
        del pos[len(pos)-1]

    return pos

def verifica_colisao(corpo):
    i=0
    for x in corpo:
        if corpo[0]==x:
            i+=1
    if i>=2:
        return True
    else:
        return False

def altera_direcao(atual,novo):
    if (atual=="C" and novo=="B") or (atual=="B" and novo=="C") or (atual=="E" and novo=="D") or (atual=="D" and novo=="E"):
        return atual
    else:
        return novo

def cobra_vai_comer(pos,comida,direcao):
    if direcao=="C":
        cabeca=[pos[0][0]-1, pos[0][1]]
    if direcao=="B":
        cabeca=[pos[0][0]+1, pos[0][1]]
    if direcao=="E":
        cabeca=[pos[0][0], pos[0][1]-1]
    if direcao=="D":
        cabeca=[pos[0][0], pos[0][1]+1]

    if cabeca==comida:
        return True
    else:
        return False

def verifica_vitoria(pos,tamanho):
    if len(pos)==tamanho**2:
        return True
    else:
        return False

from funcoes import *
import random

tamanho=int(input("> Digite o tamanho do tabuleiro: "))
pos=[[0, 2], [0, 1], [0, 0]]
direcao_antiga="D"
comida_antiga=[2,2]

print(desenha_tabuleiro(pos, comida_antiga, direcao_antiga, tamanho))

while verifica_colisao(pos)==False and verifica_vitoria(pos,tamanho)==False:
    direcao_nova=input("> Digite a nova direção (w, a, s, d): ")
    while direcao_nova not in ("w","s","a","d"):
        print("Direção inválida! Use w, a, s, d.")
        direcao_nova=input("> Digite a nova direção (w, a, s, d): ")
    if direcao_nova=="w":
        direcao_nova="C"
    if direcao_nova=="s":
        direcao_nova="B"
    if direcao_nova=="a":
        direcao_nova="E"
    if direcao_nova=="d":
        direcao_nova="D"
        
    direcao_nova=altera_direcao(direcao_antiga,direcao_nova)

    if cobra_vai_comer(pos,comida_antiga,direcao_nova)==True:
        comida_nova=[random.randint(0,tamanho-1),random.randint(0,tamanho-1)]
    else:
        comida_nova=comida_antiga

    pos=movimenta_cobra(pos, direcao_nova,cobra_vai_comer(pos,comida_antiga,direcao_nova),tamanho)

    if verifica_colisao(pos)==False and verifica_vitoria(pos,tamanho)==False:
        print(desenha_tabuleiro(pos, comida_nova, direcao_nova, tamanho))

    direcao_antiga=direcao_nova
    comida_antiga=comida_nova

if verifica_colisao(pos)==True:
    print("Fim de jogo! A cobra colidiu consigo mesma.")
    
elif verifica_vitoria(pos,tamanho)==True:
    print("Parabéns! Você venceu o jogo.")
