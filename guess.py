#Эта игра по угадыванию чисел.

import random
guesssesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()
number = random.randint(1, 20)
print('Что ж, ' + myName + ', я загадываю число о т1 до 20.')

for guessesTaken in range (6):
    print('Попробуй угадать.')
    guess =  int(input())

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Загаданное число ' + number + '.')

                
