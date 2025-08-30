from time import sleep
mes=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
print(mes[0])
dia= {"janeiro":31,"fevereiro":28,"março":31,"abril":30,"maio":31,"junho":30,"julho":31,"agosto":31,"setembro":30,"outubro":31,"novembro":30,"dezembro":31}
cadastro=dict()
informacoes=dict()
print("=== Cadastro pessoal ===")
cadastro["nome"]=str(input("Nome: "))
while True:
    cadastro["dia"]=int(input("Dia: "))
    cadastro["mês"]=input("Mês: ")
    if cadastro["mês"].isnumeric():
        if int(cadastro["mês"])>12:
            print("\033[31mEsse mês é invalido!\033[m Tente novamente")
        else:
            break
    elif not cadastro["mês"].isnumeric():
        if cadastro["mês"] not in mes:
            print("\033[31mEsse mês é invalido!\033[m Tente novamente")
            continue
        elif dia[cadastro["mês"]]<cadastro["dia"]:
            print("\033[31mDia inválido!\033[m Tente novamente")
            continue
        else:
            m=0
            for c in mes:
                m+=1
                if c==cadastro["mês"]:
                    cadastro["mês"]=m
            break
while True:
    cadastro["ano"]=int(input("Ano: "))
    if cadastro["ano"]>2025:
        print("\033[31mAno inválido!\033[m Tente novamente")
        continue
    else:
        break
while True:
    cadastro["email"]=str(input("Email: "))
    if "@gmail.com" not in cadastro["email"]:
        print("\033[31mEmail inválido!\033[m Tente novamente")
        continue
    else:
        break
cadastro["senha"]=str(input("Senha: "))
while True:
    cadastro["confirmar"]=str(input("Confirmar senha: "))
    if cadastro["confirmar"]!=cadastro["senha"]:
        print("\033[31mSenha diferente da original!\033[m Tente novamente")
        continue
    else:
        break
print("\nColetando informacoes",end='')
for c in range(0,3):
    print(".",end=''if c<3 else ".")
    sleep(0.4)
print("\n\n=== Login ===")
while True:
    informacoes["email"]=str(input("Email: "))
    informacoes["senha"]=str(input("Senha: "))
    if informacoes["email"]!=cadastro["email"] or informacoes["senha"]!=cadastro["senha"]:
        print("\033[31mEmail ou senha incorretos!\033[m Tente novamente")
        continue
    else:
        break
print("\n=== Informações ===")
print(f"Nome: {cadastro['nome'].title()}")
print(f"idade: {2025-cadastro["ano"]} anos (",end="")
print(f"0{cadastro['dia']}"if cadastro["dia"]<10 else f"{cadastro["dia"]}",end="")
print("/",end="")
print(f"{mes[cadastro['mês']]}" if not cadastro["mês"].isnumeric() else f"0{cadastro["mês"]}" if int(cadastro["mês"])<10 else f"{cadastro["mês"]}",end="")
print(f"/{cadastro['ano']})")
print(f"Email: {cadastro['email']}")
