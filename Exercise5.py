from random import choice

baralho=[13,2,3,4,5,6,7,8,9,10,11,12]
player=list()
pc=list()
soma_player=soma_pc=0

def Print(a):
    print("="*(len(a)+7))
    print(a)
    print("="*(len(a)+7))

def iniciar():
    global soma_player,soma_pc
    for c in range(0,2):
        player.append(choice(baralho))
        baralho.remove(player[len(player)-1])

        pc.append(choice(baralho))
        baralho.remove(pc[len(player)-1])
    for c in player:
        soma_player += c
    for c in pc:
        soma_pc += c
    print("Suas cartas >")
    for c in player:
        print(c, end=' ')

def pedir_carta(a):
    global soma_player,soma_pc
    if baralho:
        a.append(choice(baralho))
        baralho.remove(a[len(a)-1])
        if a==player:
            soma_player+=a[len(a)-1]
        else:
            soma_pc+=a[len(a)-1]
    else:
        print("Cartas do baralho insuficientes, vamos virar as cartas.")
        virar()

def virar():
    global soma_player, soma_pc
    if 13 in player:
        if soma_player>21:
            soma_player-=12
    if 13 in pc:
        if soma_pc>21:
            soma_pc-=12

    #caso sejam iguais
    if soma_pc==soma_player:
        print(f"\nEmpate!!!\nOponente > {soma_pc}\nVocê > {soma_player}")

    #caso ambos sejam negativos
    elif 21-soma_pc<0 and 21-soma_player<0:
        if 21-soma_pc>21-soma_player:
            print(f"\033[32mOponente > {soma_pc} (Vencedor)\033[m\nVocê > {soma_player}")
        elif 21-soma_pc<21-soma_player:
            print(f"Oponente > {soma_pc}\n\033[32mVocê > {soma_player} (Vencedor)\033[m")

    #caso um seja negativo
    elif 21-soma_pc<0<=21-soma_player:
        print(f"Oponente > {soma_pc}\n\033[32mVocê > {soma_player} (Vencedor)\033[m")
    elif 21-soma_pc>=0>21-soma_player:
        print(f"\033[32mOponente > {soma_pc} (Vencedor)\033[m\nVocê > {soma_player}")

    #caso ambos sejam positivos
    elif 21-soma_pc>=0<=21-soma_player:
        if 21-soma_pc<21-soma_player:
            print(f"\033[32mOponente > {soma_pc} (Vencedor)\033[m\nVocê > {soma_player}")
        elif 21-soma_pc>21-soma_player:
            print(f"Oponente > {soma_pc}\n\033[32mVocê > {soma_player} (Vencedor)\033[m")
    quit()

Print("\tVamos jogar BlackJack")
iniciar()
while True:
    resp=input("\n\nDeseja pular sua vez? ")
    if resp=="s":
      #verificando se a máquina acha válido puxar mais uma carta
        if soma_pc<17:
            pedir_carta(pc)
            print("\nOponente pediu uma carta",end='')
        else:
            print("\nOponente passou a vez.\n")
            Print("\tVirando as cartas")
            virar()
    elif resp=="n":
        pedir_carta(player)
        print("\nSuas cartas >")
        for c in player:
            print(c, end=' ')
        if soma_pc<17:
            pedir_carta(pc)
            print("\n\nOponente pediu uma carta",end='')
        else:
            print("\n\nOponente passou a vez.",end='')
    else:
        print("\033[31mResposta inválida, tente novamente.\033[m")
