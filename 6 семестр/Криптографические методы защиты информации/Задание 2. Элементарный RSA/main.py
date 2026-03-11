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
    # p, q, N, e, d = 17, 19, 323, 3, 108
    # Случайно выбранные p=17 и q=19
    # Значит, N=p*q=17*19=323
    # Следовательно phi(323)=(p-1)*(q-1)=16*18=288
    # Берем число e=3
    # При e=3 невозможно найти подходящий d
    """
    e, phi = 3, 288
    for d in range(1, 1000):
        if (d * e) % phi == 1:
            print(d)
    """
    p, q, N, e, d = 17, 19, 323, 5, 173
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
