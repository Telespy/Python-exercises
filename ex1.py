from random import randint
class jogo:
    def __init__(self,nick):
        self.num=randint(1,100)
        self.nick = nick

    def jogar(self,tent):
        esq = 'y'
        while esq == 'y':
            guess=0
            print(f"\n\033[32mWelcome {self.nick.title()}, to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nAnd if you want a hint, just type '0'.\n")
            print('Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n')
            esc=0
            while esc not in [1,2,3]:
                esc = int(input('Enter your choice: '))
                if esc>3 or esc<1:
                    print('Sorry, you have selected an invalid choice.')
            if esc==1:
                print('Great! You have selected the Easy difficulty Level.')
            elif esc==2:
                print('Great! You have selected the Medium difficulty Level.')
            elif esc==3:
                print('Great! You have selected the Hard difficulty Level.')
            list={1:10,2:5,3:3}
            self.dif=list[esc]

            print("let's start the Game!\n")
            while guess!=self.num and esq=='y':
                guess=int(input('Enter your guess: '))
                if guess>100:
                    print(f'This guess is not valid.\n')
                elif guess == 0:
                    print(f'The number you are looking for is {'even' if self.num % 2 == 0 else 'odd'}.\n')
                else:
                    tent+=1
                    if guess==self.num:
                        print('Congratulations! You guessed the correct number in', f'{tent} attempts.' if tent>1 else f'{tent} attempt.\n')
                        esq=input('Do you want to play again? (y/n): '.lower())
                        break
                    elif guess>self.num:
                        print(f'Incorrect! The number is less than {guess}. {self.dif-tent} attempts remaining\n')
                    elif guess<self.num:
                        print(f'Incorrect! The number is greater than {guess}. {self.dif-tent} attempts remaining\n')
                    if tent==self.dif and guess!=self.num:
                        print(f'Sorry, you have exhausted your attempts. The correct number was {self.num}')
                        esq = input('Do you want to play again? (y/n): '.lower())
        print('Thank you for playing!')

player1=jogo(input('Enter your nick: '))
player1.jogar(0)
