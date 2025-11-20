from bbs_generator import bbs_generator


def process_file(input_name, output_name, mode='encrypt'):
    language = {
        'А': '000000', 'Б': '000001', 'В': '000010', 'Г': '000011',
        'Д': '000100', 'Е': '000101', 'Ё': '000110', 'Ж': '000111',
        'З': '001000', 'И': '001001', 'Й': '001010', 'К': '001011',
        'Л': '001100', 'М': '001101', 'Н': '001110', 'О': '001111',
        'П': '010000', 'Р': '010001', 'С': '010010', 'Т': '010011',
        'У': '010100', 'Ф': '010101', 'Х': '010110', 'Ц': '010111',
        'Ч': '011000', 'Ш': '011001', 'Щ': '011010', 'Ъ': '011011',
        'Ы': '011100', 'Ь': '011101', 'Э': '011110', 'Ю': '011111',
        'Я': '100000', 'A': '100001', 'B': '100010', 'C': '100011',
        'D': '100100', 'E': '100101', 'F': '100110', 'G': '100111',
        'H': '101000', 'I': '101001', 'J': '101010', 'K': '101011',
        'L': '101100', 'M': '101101', 'N': '101110', 'O': '101111',
        'P': '110000', 'Q': '110001', 'R': '110010', 'S': '110011',
        'T': '110100', 'U': '110101', 'V': '110110', '—': '110111',
        '!': '111000', ';': '111001', ':': '111010', '-': '111011',
        ' ': '111100', ',': '111101', '.': '111110', '?': '111111',
    }
    with open(input_name, 'r', encoding='utf-8') as f:
        text_input = f.readline().upper()
    text_bits = ''.join(language[c] for c in text_input)

    if mode == 'encrypt':
        gamma, p, q, X = bbs_generator(len(text_bits))
        result_bits = ''.join('1' if text_bits[i] != gamma[i] else '0' for i in range(len(text_bits)))
        with open(output_name + '.key', 'w') as f:
            f.write(f"{p}\n{q}\n{X}")
        message = f"Файл успешно зашифрован! Ключ сохранен в {output_name}.key"

    elif mode == 'decrypt':
        try:
            with open(input_name + '.key', 'r') as f:
                p = int(f.readline().strip())
                q = int(f.readline().strip())
                X = int(f.readline().strip())
        except FileNotFoundError:
            return "Ошибка: файл ключа не найден!"
        gamma, _, _, _ = bbs_generator(len(text_bits), p, q, X)
        result_bits = ''.join('1' if text_bits[i] != gamma[i] else '0' for i in range(len(text_bits)))
        message = "Файл успешно расшифрован!"

    reverse_language = {v: k for k, v in language.items()}
    text_output = ''.join(reverse_language[result_bits[i:i + 6]] for i in range(0, len(result_bits), 6))
    with open(output_name, 'w', encoding='utf-8') as f:
        f.write(text_output)
    return message


def main():
    while True:
        print("1. Зашифровать файл")
        print("2. Расшифровать файл")
        print("3. Выход")

        choice = input("Выберите действие: ")
        if choice == '1':
            input_file = input("Входной файл: ")
            output_file = input("Выходной файл: ")
            result = process_file(input_file, output_file, 'encrypt')
            print(result)
        elif choice == '2':
            input_file = input("Входной файл: ")
            output_file = input("Выходной файл: ")
            result = process_file(input_file, output_file, 'decrypt')
            print(result)
        elif choice == '3':
            break
        else:
            print("Неверный выбор!")


if __name__ == '__main__':
    main()
