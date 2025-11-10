def create_gamma(open_text: str) -> str:
    return '1' * len(open_text)

def add(text_in: str, gamma: str) -> str:
    text_out = gamma
    for i in range(len(text_in)):
        if text_in[i] == gamma[i]:
            text_out = text_out[:i] + '0' + text_out[i+1:]
    return text_out

def main(input_name, output_name):
    file_input = open(input_name, 'r', encoding='utf-8')
    text_input = file_input.readline()
    file_input.close()
    text_input = text_input.upper()
    language = {
        'А': '000000',
        'Б': '000001',
        'В': '000010',
        'Г': '000011',
        'Д': '000100',
        'Е': '000101',
        'Ё': '000110',
        'Ж': '000111',
        'З': '001000',
        'И': '001001',
        'Й': '001010',
        'К': '001011',
        'Л': '001100',
        'М': '001101',
        'Н': '001110',
        'О': '001111',
        'П': '010000',
        'Р': '010001',
        'С': '010010',
        'Т': '010011',
        'У': '010100',
        'Ф': '010101',
        'Х': '010110',
        'Ц': '010111',
        'Ч': '011000',
        'Ш': '011001',
        'Щ': '011010',
        'Ъ': '011011',
        'Ы': '011100',
        'Ь': '011101',
        'Э': '011110',
        'Ю': '011111',
        'Я': '100000',
        'A': '100001',
        'B': '100010',
        'C': '100011',
        'D': '100100',
        'E': '100101',
        'F': '100110',
        'G': '100111',
        'H': '101000',
        'I': '101001',
        'J': '101010',
        'K': '101011',
        'L': '101100',
        'M': '101101',
        'N': '101110',
        'O': '101111',
        'P': '110000',
        'Q': '110001',
        'R': '110010',
        'S': '110011',
        'T': '110100',
        'U': '110101',
        'V': '110110',
        'W': '110111',
        'X': '111000',
        'Y': '111001',
        'Z': '111010',
        ' ': '111011',
        ',': '111100',
        '.': '111101',
        '?': '111110',
        '!': '111111',
    }
    text_bites = ""
    for i in text_input:
        text_bites += language[i]
    gamma = create_gamma(text_bites)
    text_bites = add(text_bites, gamma)
    text_output = ""
    while text_bites:
        symbol_bites = text_bites[:6]
        text_bites = text_bites[6:]
        for key, value in language.items():
            if value == symbol_bites:
                text_output += key
    file_output = open(output_name, 'w', encoding='utf-8')
    file_output.write(text_output)
    file_output.close()

if __name__ == '__main__':
    main(str(input("Входной файл:  ")), str(input("Выходной файл: ")))
