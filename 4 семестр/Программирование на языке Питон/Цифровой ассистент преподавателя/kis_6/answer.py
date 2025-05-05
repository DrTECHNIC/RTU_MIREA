# Самое популярное решение
"""def main(array_B):
    array_I = {(4 * symbol_beta - symbol_beta) for symbol_beta in array_B
               if symbol_beta < 57}
    array_Z = {symbol_beta for symbol_beta in array_B
               if (symbol_beta <= 88) ^ (symbol_beta >= -42)}
    array_A = {(symbol_yota % 3 - symbol_yota) for symbol_yota in array_I
               if (symbol_yota > -95) ^ (symbol_yota <= 72)}
    array_EPH = {symbol_zeta for symbol_zeta in array_Z
                 if (symbol_zeta > -14) ^ (symbol_zeta <= 27)}
    sum_1 = sum(abs(symbol_phi) for symbol_phi in array_EPH)
    sum_2 = sum((symbol_phi * symbol_alpha) for symbol_phi in array_EPH
                for symbol_alpha in array_A)
    result_ro = sum_1 - sum_2
    return result_ro"""

# 2-е по популярности решение
"""def create_array_I(array_B):
    array_I = []
    for symbol_beta in array_B:
        if symbol_beta < 57:
            array_I.append(4 * symbol_beta - symbol_beta)
    return array_I


def create_array_Z(array_B):
    array_Z = []
    for symbol_beta in array_B:
        if (symbol_beta <= 88) ^ (symbol_beta >= -42):
            array_Z.append(symbol_beta)
    return array_Z


def create_array_A(array_I):
    array_A = []
    for symbol_yota in array_I:
        if (symbol_yota > -95) ^ (symbol_yota <= 72):
            array_A.append(symbol_yota % 3 - symbol_yota)
    return array_A


def create_array_EPH(array_Z):
    array_EPH = []
    for symbol_zeta in array_Z:
        if (symbol_zeta > -14) ^ (symbol_zeta <= 27):
            array_EPH.append(symbol_zeta)
    return array_EPH


def main(array_B):
    array_I = create_array_I(array_B)
    array_Z = create_array_Z(array_B)
    array_A = create_array_A(array_I)
    array_EPH = create_array_EPH(array_Z)
    sum_1 = sum(abs(symbol_phi)
                for symbol_phi in array_EPH)
    sum_2 = sum((symbol_phi * symbol_alpha)
                for symbol_phi in array_EPH
                for symbol_alpha in array_A)
    result_ro = sum_1 - sum_2
    return result_ro"""


if __name__ == "__main__":
    print("main({-92, -27, 5, 44, 13, -83, 54, 23, 24, 91}) =",
          main({-92, -27, 5, 44, 13, -83, 54, 23, 24, 91}))
    print("main({-59, -23, -49, -81, 48, 50, -45, 84, 24, -97}) =",
          main({-59, -23, -49, -81, 48, 50, -45, 84, 24, -97}))