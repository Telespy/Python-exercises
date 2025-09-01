from random import choice
from time import sleep
from string import ascii_lowercase
cont=0
temas=["cor","carro","cidade","animal","objeto"]
letra=choice(ascii_lowercase)
usuario={"cor":"", "carro":"", "cidade":"", "animal":"", "objeto":"","ponto":0}
sistema={"cor":"", "carro":"", "cidade":"", "animal":"", "objeto":"","ponto":0}
jogadores=["usuario","sistema"]
players=[usuario,sistema]

def printar(a):
    print("="*(len(a)+8))
    print(f"\t{a}")
    print("="*(len(a)+8))

def listar(a):
    printar("Lista de itens")
    cont2=0
    for b in players:
        cont3=0
        print(f"\n\033[32m{jogadores[cont2].upper()}\033[m")
        for d in temas:
            print(f"{d} > ",end='')
            b[d]=input()
            cont3+=1
        cont2+=1


def verificar():
    for c in temas:
        if usuario[c]==sistema[c]:
            if usuario[c][0]!=letra:
                print("\nAmbos jogadores erraram essa rodada, menos um ponto de cada")
                usuario["ponto"]-=1
                sistema["ponto"]-=1
            else:
                print("\nEssa rodada foi empate, 1 ponto para cada")
                usuario["ponto"]+=1
                sistema["ponto"]+=1
        elif usuario[c][0]!=letra and sistema[c][0]!=letra:
            print("\nAmbos jogadores erraram essa rodada, menos um ponto de cada")
            usuario["ponto"]-=1
            sistema["ponto"]-=1
        elif usuario[c][0]!=letra:
            print("\nsistema levou a melhor, mais 3 pontos")
            sistema["ponto"]+=3
        elif sistema[c][0]!=letra:
            print("\nusuario levou a melhor, mais 3 pontos")
            usuario["ponto"]+=3
        else:
            print("\nAmbos jogadores pontuaram, mais 3 pontos para cada")
            usuario["ponto"]+=3
            sistema["ponto"]+=3
        sleep(1)
    if usuario["ponto"]<0:
        usuario["ponto"]=0
    if sistema["ponto"]<0:
        sistema["ponto"]=0


printar("Jogo Stop")
print(f"\nA letra escolhida foi > {letra}\n")
listar(letra)
printar("Verificando pontuações")
verificar()
printar("Pontuação dos jogadores")
for c in players:
    print(f"{jogadores[cont].title()} pontos: {c["ponto"]}")
    cont+=1
