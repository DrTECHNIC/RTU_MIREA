def encrypt(open_text, e, N):
    cipher_text = []
    for m in open_text:
        if m >= N:
            raise ValueError(f"Символ {chr(m)} имеет код {m}, что больше или равно модулю N={N}. Он не может быть зашифрован.")
        c = m ** e % N
        cipher_text.append(c)
    return cipher_text

def decrypt(cipher_text, d, N):
    open_text = []
    for c in cipher_text:
        if c >= N:
            raise ValueError(f"Число {c} должно быть меньше модуля N={N}.")
        m = c ** d % N
        open_text.append(chr(m))
    return ''.join(open_text)

def main():
    p, q, N, e, d = 17, 19, 323, 11, 131
    while True:
        print("1 - Зашифровать текст")
        print("2 - Расшифровать шифртекст")
        match input("Ваш выбор: "):
            case '1':
                try:
                    text_input = [ord(x) for x in input("Введите открытый текст: ")]
                    text_output = encrypt(text_input, e, N)
                    print("Шифртекст:")
                    print(' '.join(str(num) for num in text_output))
                except ValueError as error: print(error)
            case '2':
                try:
                    text_input = [int(x) for x in input("Введите шифртекст: ").split()]
                    text_output = decrypt(text_input, d, N)
                    print("Открытый текст:")
                    print(text_output)
                except ValueError as error: print(error)
            case _:
                break

if __name__ == "__main__":
    main()
