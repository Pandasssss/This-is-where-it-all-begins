def main():
    import random
    mysterious_num = random.randint(1,100)
    print('Добро пожаловать в числовую угадайку')
    n = input('Введите число: ')
    is_valid(n)
    
def is_valid(n):
    if n.isdigit() and int(n) in range(1,101):
        return True
    return False

main()
