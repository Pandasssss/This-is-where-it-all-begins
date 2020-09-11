import random

def main():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    try:
        cntPw = int(input('Укажите количество паролей для генерации: '))
        lenPw = int(input('Укажите длину одного пароля: '))
    except:
        print('Вводи числа, муд@к')
        main()
        return
    dig_on = input('Включать ли цифры 0123456789? (y/n)')
    ABC_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
    abc_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
    ch_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
    exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
    
main()