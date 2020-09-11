import random

def main():
    print('Добро пожаловать в числовую угадайку')
    main_cycle()
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

def main_cycle():
    max_num = input('Из скольки чисел угадываем, сударь? ')
    while not max_num.isdigit():
        max_num = input('А может быть все-таки введем целое число? ')
    max_num = int(max_num)
    mysterious_num = random.randint(1, max_num)
    n = None
    count = 0
    while n != mysterious_num:
        n = input('Введите число: ')
        if not is_valid(n, max_num):
            print(f'А может быть все-таки введем целое число от 1 до {max_num}?')
            continue
        count += 1
        n = int(n)
        if n < mysterious_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > mysterious_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == mysterious_num:
            print(f'Вы угадали, поздравляем! Количество попыток: {count}')
        else:
            print('Strange Error')
    if input('Хотите сыграть еще? y - да, n - нет ') == 'y':
        main_cycle()

def is_valid(n, max_num):
    if n.isdigit() and int(n) in range(1, max_num + 1):
        return True
    return False

main()
