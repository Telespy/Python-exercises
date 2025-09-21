from random import randint

class calculadora():
    def __init__(self,n1,n2,op):
        self.n1 = n1
        self.n2 = n2
        self.op = op
    def calculo(self):
        if self.op=='+':
            return self.n1 + self.n2
        elif self.op == '-':
            return self.n1 - self.n2
        elif self.op == '/':
            return self.n1 / self.n2
        elif self.op == '*':
            return self.n1 * self.n2
        elif self.op == '**':
            return self.n1 ** self.n2
        elif self.op == '//':
            return self.n1 // self.n2
        elif self.op == '%':
            return self.n1 % self.n2
        else:
            return None

num1=int(input("Primeiro valor: "))
num2=int(input("Segundo valor: "))
print("\n(+) soma\n(-) subtração\n(/) divisão\n(*) multiplicação\n(//) divisão direta\n(**) exponenciação\n(%) resto da divisão")
while True:
    operador=input("\nQual operador deseja usar? ")
    if not operador in ['+','-','/','*','//','%']:
        print("Esse operador é inválido!")
    else:
        cal=calculadora(num1,num2,operador)
        print(f"\nResultado > {cal.calculo()}")
        break
