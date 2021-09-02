import random
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''','''
   +---+
   o   |
       |
       |
      ===''','''
   +---+
   o   |
   |   |
       |
      ===''','''
   +---+
   o   |
  /|   |
       |
      ===''','''
   +---+
   o   |
  /|\  |
       |
      ===''','''
   +---+
   o   |
  /|\  |
       |
      ===''','''
   +---+
   o   |
  /|\  |
  /    |
      ===''','''
   +---+
   o   |
  /|\  |
  / \  |
      ===''','''
   +---+
  [o   |
  /|\  |
  / \  |
      ===''','''
   +---+
  [o]  |
  /|\  |
  / \  |
      ===''']
words = {'животные':'''аист акула бабуин баран барсук бобр бык верблюд волк
воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка
кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь
моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел
панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка
форель хорек черепаха ястреб ящерица'''.split(), 'цвета': '''красный оранжевый
желтый зеленый синий голубой фиолетовый белый черный коричневый'''.split(),
'фигуры':'''квадрат треугольник прямоугольник круг эллипс ромб трапеция
параллелограмм пятиугольник шестиугольник восьмиугольник'''.split(),
'фрукты':'''яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик
банан абрикос манго банан нектарин'''.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex],wordKey

def displayBoard(missedLeters, correctLeters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок
    # ввел только одну букву и ничего больше.
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

def playAgain():
    # Эта функция возвращает значение True, если игрок хочет сыграть заново; в
    # противном случае возвращает False.
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')

def choiceDifficulty():
    difficulty = ''
    pictureNew = HANGMAN_PICS.copy()
    plen = len(pictureNew)
    hlen = len(HANGMAN_PICS)
    print('Выберите уровень сложности: Л - легкий, С - средний, Т - тяжелый')
    difficulty = input().upper()
    while (difficulty not in 'ЛСТ') or (difficulty == ''):
        print('Пожалуйста, введите одну из букв: Л, С или Т')
        difficulty = input().upper()
    if difficulty == 'С':
        del pictureNew[8]
        del pictureNew[7]
        return pictureNew
    if difficulty == 'Т':
        del pictureNew[8]
        del pictureNew[7]
        del pictureNew[5]
        del pictureNew[3]
        return pictureNew
        
hangmanPicture = choiceDifficulty()
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

print('В И С Е Л И Ц А')

while True:
    print('Секретное слово из набора: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters += guess

        if len(missedLetters) == len(list(hangmanPicture)) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНе угадано букв:' + str(len(missedLetters)) + ' и угадано букв:' + str(len(correctLetters)) + '. Было загадано слово"' + secretWord + '".')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
            hangmanPicture = choiceDifficulty()
        else:
            break
