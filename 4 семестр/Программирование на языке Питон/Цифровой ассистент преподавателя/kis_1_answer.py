# Ниже представлены 4 варианта решения задачи для функции, представленной на скриншоте

def main(y):
    # 1/4
    # 1) Импорт целой библиотеки math и использование нужных функций.
    # 2) Возврат целого выражения.
    import math
    return ((93 * math.pow(y, 3) / (41 * math.pow(y, 4) +
            3 * math.pow(math.cos(y), 5))) -
            (math.pow(math.asin(y), 3)) / 99 - 31 * math.pow(y, 2))

    # 2/4
    # 1) Импорт только нужных функций из библиотеки math.
    # 2) Возврат всего выражения сразу.
    from math import pow, cos, asin
    return ((93 * pow(y, 3) / (41 * pow(y, 4) + 3 *
            pow(cos(y), 5))) - (pow(asin(y), 3)) / 99 - 31 * pow(y, 2))

    # 3/4
    # 1) Импорт целой библиотеки math и использование нужных функций.
    # 2) Расчёт значений по частям и возврат итоговой результата.
    import math
    part_1 = (93 * math.pow(y, 3)) / (41 * math.pow(y, 4) + 3 * math.pow(math.cos(y), 5))
    part_2 = math.pow(math.asin(y), 3) / 99 - 31 * math.pow(y,2)
    return part_1 - part_2

    # 4/4
    # 1) Импорт только нужных функций из библиотеки math.
    # 2) Расчёт значений по частям и возврат итоговой результата.
    from math import pow, cos, asin
    part_1 = (93 * pow(y, 3)) / (41 * pow(y, 4) + 3 * pow(cos(y), 5))
    part_2 = pow(asin(y), 3) / 99 - 31 * pow(y, 2)
    return part_1 - part_2


if __name__ == "__main__":
    print("main(0.85) ≈", main(0.85))
    print("main(0.62) ≈", main(0.62))
    print("main(0.74) ≈", main(0.74))
    print("main(-0.26) ≈", main(-0.26))
    print("main(0.63) ≈", main(0.63))
