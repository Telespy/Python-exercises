from datetime import datetime

def today():
    today=datetime.now()
    return today
def verify_date(date):
    try:
        date_format=datetime.strptime(date,"%d/%m/%Y")
        return date_format
    except:
        print("\n\033[31mEntrada inválida!\033[m\nFormato sugerido: D/M/Y.\nExemplo: 01/02/2000 ou 1/2/2000")
        quit()
def verify(date_ref):
    due_date=verify_date(date_ref)
    if today()<due_date:
        return "\nProduto dentro da data de validade"
    else:
        return "\nProduto vencido"

print("Qual a data de vencimento do produto?\nFormato válido: D/M/Y.\nExemplo: 01/02/2000 ou 1/2/2000\n")
print(verify(input("")))
