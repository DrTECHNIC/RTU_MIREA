import math


# Самое популярное решение
"""def main(z):
    if z < 47:
        return math.pow(math.ceil(math.pow(z, 3) + 79), 2) / 89
    if 47 <= z < 117:
        return math.pow(97 * z - 2 * math.pow(z, 3), 3)
    if 117 <= z < 195:
        return 89 * math.pow(29 * z + math.pow(z, 2), 4)
    if 195 <= z < 232:
        return 30 * math.pow(z, 3) + math.pow(z, 7) + 85
    if z >= 232:
        return (math.pow(math.atan(10 * z + 3 * math.pow(z, 2) + 1), 4) -
                math.pow(math.tan(18 * math.pow(z, 2)), 6))"""


# 2-е по популярности решение
"""def main(z):
    return (
        (z < 47) * (math.ceil(z ** 3 + 79)) ** 2 / 89 +
        (47 <= z < 117) * ((97 * z - 2 * z ** 3) ** 3) +
        (117 <= z < 195) * (89 * (29 * z + z ** 2) ** 4) +
        (195 <= z < 232) * (30 * z ** 3 + z ** 7 + 85) +
        (z >= 232) * math.atan(10 * z + 3 * z ** 2 + 1) ** 4 -
        (z >= 232) * math.tan(18 * z ** 2) ** 6
    )"""

# 3-е по популярности решение
"""def main(z):
    conditions = {
        z < 47: lambda: (math.ceil(z ** 3 + 79)) ** 2 / 89,
        47 <= z < 117: lambda: (97 * z - 2 * z ** 3) ** 3,
        117 <= z < 195: lambda: 89 * (29 * z + z ** 2) ** 4,
        195 <= z < 232: lambda: 30 * z ** 3 + z ** 7 + 85,
        z >= 232: lambda: ((math.atan(10 * z + 3 * z ** 2 + 1)) ** 4
                           - (math.tan(18 * z ** 2)) ** 6)
    }
    for condition, expression in conditions.items():
        if condition:
            return expression()"""


if __name__ == "__main__":
    print("main(261) =", main(261))
    print("main(104) =", main(104))
    print("main(236) =", main(236))
    print("main(25) =", main(25))
    print("main(86) =", main(86))
