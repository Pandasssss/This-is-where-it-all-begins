def main():
    import random
    mysterious_num = random.randint(1,100)
    print('Добро пожаловать в числовую угадайку')
    while True:
        n = input('Введите число: ')
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if n == mysterious_num:
            print('Yap')
            break
    
def is_valid(n):
    if n.isdigit() and int(n) in range(1,101):
        return True
    return False

main()
