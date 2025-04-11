# Самое популярное решение
"""import re

def main(input_string):
    content_match = re.search(r'\\begin(.*?)\\end', input_string, re.DOTALL)
    if not content_match:
        return {}
    content = content_match.group(1).strip()
    matches = re.findall(r'do\s+loc\s+(-?\d+)\s*->\s*(\w+);', content)
    result = {name: int(number) for number, name in matches}
    return result"""


# 2-е по популярности решение
"""def main(input_string: str):
    input_string = input_string.replace('\n', ' ')
    content = input_string.split('\\begin')[1].split('\\end')[0].strip()
    result = {}
    for entry in content.split("done,"):
        if entry == '':
            break
        entry = entry.strip().lstrip('do loc ').rstrip(';').strip()
        value, key = entry.split('->', 1)
        result[key.strip()] = int(value.strip())
    return result"""


if __name__ == "__main__":
    print(main("\\begin do loc 7320 -> beorri_31;done, do loc 8341 -> tetege; done, do"
               "loc -2915 ->xelea;done, do loc -7075 -> raen;done, \\end"))
    print(main("\\begin do loc -3930 ->maatve_639; done, do loc -6290 -> zain_107; done, \\end"))