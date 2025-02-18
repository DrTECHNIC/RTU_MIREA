# Самое популярное решение
"""def main(b, n):
    mult = 1
    for c in range(1, n+1):
        sum = 0
        for k in range(1, b+1):
            part1 = 5 + 14 * (39 * k - c ** 2 / 37) ** 2
            part2 = 3 * (0.02 - 82 * c ** 2 - 10 * k)
            sum += (part1 + part2)
        mult *= sum
    return mult"""


# 2-е по популярности решение
"""from math import prod


def main(b, n):
    def calculate_sum(c):
        return sum(5 + 14 * (39 * k - c ** 2 / 37) ** 2 +
                   3 * (0.02 - 82 * c ** 2 - 10 * k)
                   for k in range(1, b + 1))
    return prod(calculate_sum(c) for c in range(1, n + 1))"""


# Не существующее по популярности решение
"""def sum(b, c, k=1):
    if k > b:
        return 0
    else:
        return (5 + 14 * (39 * k - c ** 2 / 37) ** 2 +
                3 * (0.02 - 82 * c ** 2 - 10 * k)) + sum(b, c, k + 1)


def mult(b, n, c=1):
    if c > n:
        return 1
    else:
        return sum(b, c) * mult(b, n, c + 1)


def main(b, n):
    return mult(b, n)"""

# 4-е по популярности решение
"""def main(b, n):
    mult = 1
    c = 1
    while c < n + 1:
        sum = 0
        k = 1
        while k < b + 1:
            sum += (5 + 14 * (39 * k - c ** 2 / 37) ** 2 +
                    3 * (0.02 - 82 * c ** 2 - 10 * k))
            k += 1
        mult *= sum
        c += 1
    return mult"""

# 5-е по популярности решение
"""def main(b, n):
    mult = 1
    for c in range(1, n+1):
        sum = 0
        for k in range(1, b+1):
            sum += (5 + 14 * (39 * k - c ** 2 / 37) ** 2 +
                    3 * (0.02 - 82 * c ** 2 - 10 * k))
        mult *= sum
    return mult"""


if __name__ == "__main__":
    print("main(4, 6) ≈", main(4, 6))
    print("main(4, 5) ≈", main(4, 5))
    print("main(3, 6) ≈", main(3, 6))
    print("main(4, 7) ≈", main(4, 7))
    print("main(7, 6) ≈", main(7, 6))
