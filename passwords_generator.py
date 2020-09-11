import random

def main():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
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
    chars = generate_chars(((digits, dig_on), (lowercase_letters, abc_on), (uppercase_letters, ABC_on), (punctuation, ch_on)))
    if chars == None:
        main()
        return
    print(chars)
    
def generate_chars(tpl):
    chars = ''
    for element, i in tpl:
        if i == 'y':
            chars += element
        elif i != 'n':
            print('Опять фигню ввел, давай по новой')
            return
    exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n or any symbol)')
    if exc_on == 'y':
        chars_list = list(chars)
        for charm in 'il1Lo0O':
            if charm in chars_list:
                chars_list.remove(charm)
        chars = str(chars_list)
    return chars
    
main()