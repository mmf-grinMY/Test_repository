import sys

SYMBOLS = ' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать, расшифровать или взломать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р', 'взломать', 'в']:
            return mode
        else:
            print('Введите "зашифровать" или "з" для зашифровки, "расшифровать" или "р" для расшифровки или "взломать" или "в" для взлома')
def getMessage():
    print('Введите текст: ')
    return input()

def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= MAX_KEY_SIZE:
                symbolIndex -= MAX_KEY_SIZE
            elif symbolIndex < 0:
                symbolIndex += MAX_KEY_SIZE

        translated += SYMBOLS[symbolIndex]
    return translated

def Exit():
    print('Хотите продолжить зашифровку/расшифровку текста? (да или нет)')
    if input().lower().startswith('д'):
        return 0
    else:
        sys.exit()
while True:
    mode = getMode()
    message = getMessage()
    if mode[0] != 'в': 
        key = getKey()
    print('Преобразованный текст:')
    if mode[0] != 'в':
        print(getTranslatedMessage(mode, message, key))
    else:
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, getTranslatedMessage('расшифровать', message, key))
    if Exit() != 0:
        sys.exit()

    
