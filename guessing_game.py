def main():
    import random
    mysterious_num = random.randint(1,100)
    print('Добро пожаловать в числовую угадайку')
    n = None
    while n != mysterious_num:
        n = input('Введите число: ')
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        n = int(n)
        if n < mysterious_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > mysterious_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == mysterious_num:
            print('Вы угадали, поздравляем!')
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    
def is_valid(n):
    if n.isdigit() and int(n) in range(1,101):
        return True
    return False

main()
