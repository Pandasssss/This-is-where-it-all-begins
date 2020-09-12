eng_alphabet = {'lower' : 'abcdefghijklmnopqrstuvwxyz', 'upper' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
rus_alphabet = {'lower' : "абвгдежзийклмнопрстуфхцчшщъыьэюя", 'upper' : "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"}
text = input("Введите текст для шифрования/дешифрования: ")
shift = input('Введите величину сдвига: ')
while not shift.isdigit():
    shift = input('Введи число, сука! ')
shift = int(shift)

def main():
    print(code(shift))

def code(shift: int):
    code_text = ''
    for charm in text:
        if 64 < ord(charm) < 123: # Диапазон английских букв в юникоде
            alphabet = eng_alphabet
        else:
            alphabet = rus_alphabet
        
        if charm.isupper():
            code_text += alphabet['upper'][(alphabet['upper'].index(charm) + shift) % len(alphabet['upper'])]
        elif charm.islower():
            code_text += alphabet['lower'][(alphabet['lower'].index(charm) + shift) % len(alphabet['lower'])]
        else:
            code_text += charm
    return code_text
    
main()