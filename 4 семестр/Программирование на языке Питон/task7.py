# Самое популярное решение
"""def x_0(age_1, first, second, third):
    if age_1 == 1987:
        return first
    if age_1 == 2010:
        return second
    if age_1 == 1975:
        return third


def x_1(age_2, first, second):
    if age_2 == 1970:
        return first
    if age_2 == 1990:
        return second


def x_2(word_1, first, second, third):
    if word_1 == "NCL":
        return first
    if word_1 == "EAGLE":
        return second
    if word_1 == "COBOL":
        return third


def x_3(word_2, first, second, third):
    if word_2 == "SAGE":
        return first
    if word_2 == "MQL5":
        return second
    if word_2 == "REXX":
        return third


def main(array):
    result = (
        x_2(
            array[2],
            x_1(
                array[1],
                x_3(array[3], 0, 1, 2),
                x_0(array[0], 3, 4, 5)
            ),
            x_3(
                array[3],
                x_0(array[0], 6, 7, 8),
                x_0(array[0], 9, 10, 11),
                12
            ),
            13
        )
    )
    return result"""


# 2-е по популярности решение
"""tuple = (
    {'NCL', 1970, 'SAGE'},
    {'NCL', 1970, 'MQL5'},
    {'NCL', 1970, 'REXX'},
    {'NCL', 1990, 1987},
    {'NCL', 1990, 2010},
    {'NCL', 1990, 1975},
    {'EAGLE', 'SAGE', 1987},
    {'EAGLE', 'SAGE', 2010},
    {'EAGLE', 'SAGE', 1975},
    {'EAGLE', 'MQL5', 1987},
    {'EAGLE', 'MQL5', 2010},
    {'EAGLE', 'MQL5', 1975},
    {'EAGLE', 'REXX'},
    {'COBOL'}
)


def main(r):
    s = set(r)
    return [i for i in range(len(tuple)) if not (len(tuple[i] - s))][0]"""


# 3-е по популярности решение
"""def x_0(age_1, first, second, third):
    match age_1:
        case 1987:
            return first
        case 2010:
            return second
        case 1975:
            return third


def x_1(age_2, first, second):
    match age_2:
        case 1970:
            return first
        case 1990:
            return second


def x_2(word_1, first, second, third):
    match word_1:
        case "NCL":
            return first
        case "EAGLE":
            return second
        case "COBOL":
            return third


def x_3(word_2, first, second, third):
    match word_2:
        case "SAGE":
            return first
        case "MQL5":
            return second
        case "REXX":
            return third


def main(array):
    result = (
        x_2(
            array[2],
            x_1(
                array[1],
                x_3(array[3], 0, 1, 2),
                x_0(array[0], 3, 4, 5)
            ),
            x_3(
                array[3],
                x_0(array[0], 6, 7, 8),
                x_0(array[0], 9, 10, 11),
                12
            ),
            13
        )
    )
    return result"""


# 4-е по популярности решение
"""tuple = (
    {'NCL', 1970, 'SAGE'},
    {'NCL', 1970, 'MQL5'},
    {'NCL', 1970, 'REXX'},
    {'NCL', 1990, 1987},
    {'NCL', 1990, 2010},
    {'NCL', 1990, 1975},
    {'EAGLE', 'SAGE', 1987},
    {'EAGLE', 'SAGE', 2010},
    {'EAGLE', 'SAGE', 1975},
    {'EAGLE', 'MQL5', 1987},
    {'EAGLE', 'MQL5', 2010},
    {'EAGLE', 'MQL5', 1975},
    {'EAGLE', 'REXX'},
    {'COBOL'}
)


def main(r):
    s = set(r)
    for i, v in enumerate(tuple):
        if not (len(v - s)):
            return i"""


# 5-е по популярности решение
class tree():
    def __init__(self, number, group1, after1, group2, after2, group3, after3):
        self.number = number
        self.group_first = group1
        self.after_first = after1
        self.group_second = group2
        self.after_second = after2
        self.group_third = group3
        self.after_third = after3

    def find(self, mas: list, ):
        if self.group_first == mas[self.number]:
            if type(self.after_first) == int:
                return self.after_first
            return self.after_first.find(mas)
        if self.group_second == mas[self.number]:
            if type(self.after_second) == int:
                return self.after_second
            return self.after_second.find(mas)
        if self.group_third == mas[self.number]:
            if type(self.after_third) == int:
                return self.after_third
            return self.after_third.find(mas)


def main(array):
    x213 = tree(3, 'SAGE', 0, 'MQL5', 1, 'REXX', 2)
    x210 = tree(0, 1987, 3, 2010, 4, 1975, 5)
    x21 = tree(1, 1970, x213, 1990, x210, None, None)
    x230_1 = tree(0, 1987, 6, 2010, 7, 1975, 8)
    x230_2 = tree(0, 1987, 9, 2010, 10, 1975, 11)
    x23 = tree(3, 'SAGE', x230_1, 'MQL5', x230_2, 'REXX', 12)
    x2 = tree(2, 'NCL', x21, 'EAGLE', x23, 'COBOL', 13)
    return x2.find(array)


if __name__ == "__main__":
    print("main([2010, 1970, 'NCL', 'REXX']) = ", main([2010, 1970, 'NCL', 'REXX']))
    print("main([1987, 1970, 'COBOL', 'SAGE']) =", main([1987, 1970, 'COBOL', 'SAGE']))
    print("main([1975, 1970, 'NCL', 'SAGE']) =", main([1975, 1970, 'NCL', 'SAGE']))
    print("main([1975, 1970, 'EAGLE', 'SAGE']) =", main([1975, 1970, 'EAGLE', 'SAGE']))
    print("main([1975, 1990, 'NCL', 'SAGE']) =", main([1975, 1990, 'NCL', 'SAGE']))
