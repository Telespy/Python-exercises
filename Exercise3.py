from time import sleep
gabarito={"q1":"a","q2":"a","q3":"d"}
resposta= dict()
nota=0
print("Bem vin do ao Quiz")
nome=str(input("Insira seu nome: "))
print(f"\nSeja muito bem vindo {nome}")
if input("deseja iniciar o quiz? [S/N] ")=="s":
    print("Muito bem, iniciando",end='')
    for c in range(0,3):
        print(".",end='' if c<3 else ".")
        sleep(0.4)
    print("\n\nQ. 1 Qual das seguintes opções é a forma correta de comentar várias linhas em Python?")
    print("a. '''Isto é um comentário de várias linhas'''")
    print("b. /* Isto é um comentário de várias linhas */")
    print("c. // Isto é um comentário de várias linhas")
    print("d. # Isto é um comentário de várias linhas\n")
    while True:
        resposta["q1"] = str(input("Resposta: "))
        if resposta["q1"] not in ["a", "b", "c", "d"]:
            print("\033[31mEssa resposta não condiz com as alternativas!\033[m Tente novamente")
            continue
        else:
            break
    print("\nQ. 2 O que a seguinte instrução de código imprime no console? `print(type(5 / 2))`")
    print("a. <class 'float'>")
    print("b. Um erro")
    print("c. <class 'int'>")
    print("d. 2.5\n")
    while True:
        resposta["q2"] = str(input("Resposta: "))
        if resposta["q2"] not in ["a", "b", "c", "d"]:
            print("\033[31mEssa resposta não condiz com as alternativas!\033[m Tente novamente")
            continue
        else:
            break
    print("\nQ. 3 Qual das seguintes opções é a maneira correta de definir uma função em Python?")
    print("a. create function my_function:")
    print("b. define my_function:")
    print("c. func my_function()")
    print("d. def my_function():\n")
    while True:
        resposta["q3"] = str(input("Resposta: "))
        if resposta["q3"] not in ["a", "b", "c", "d"]:
            print("\033[31mEssa resposta não condiz com as alternativas!\033[m Tente novamente")
            continue
        else:
            break
    print("\nverificando suas respostas",end='')
    for c in range(0,3):
        print(".",end='' if c<3 else ".")
        sleep(0.4)
    if resposta["q1"]==gabarito["q1"]:
        nota+=1
    if resposta["q2"]==gabarito["q2"]:
        nota+=1
    if resposta["q3"]==gabarito["q3"]:
        nota+=1
    print(f"\n{nome} nota: {nota}/3\n{(nota*100)/3:.2f}% de aproveitamento")
else:
    print("Pois bem, até a próxima")
