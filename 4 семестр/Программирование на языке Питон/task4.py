# Самое популярное решение
"""from math import floor


def main(n):
    if n == 0:
        return -0.7
    if n == 1:
        return 0.02
    return floor(1 + main(n-2) + main(n-1)**3)**3 - main(n-2) - main(n-1)**2"""

# 2-е по популярности решение
"""import math


def main(n):
    def sequence():
        a, b = -0.70, 0.02
        yield a
        yield b
        while True:
            inner = math.floor(1 + a + b ** 3)
            next_val = inner ** 3 - a - b ** 2
            a, b = b, next_val
            yield next_val
    gen = sequence()
    for _ in range(n + 1):
        result = next(gen)
    return round(result, 8)"""

# 3-е по популярности решение
"""from math import floor


def main(n):
    values = [-0.70, 0.02]
    if n < 2:
        return values[n]
    for i in range(2, n + 1):
        next_val = (floor(1 + values[i-2] + values[i-1]**3)**3
                    - values[i-2] - values[i-1]**2)
        values.append(next_val)
    return values[n]"""

# 4-е по популярности решение
"""import math


def main(n):
    match n:
        case 0:
            return -0.70
        case 1:
            return 0.02
        case _:
            prev2 = main(n - 2)
            prev1 = main(n - 1)
            inner = math.floor(1 + prev2 + prev1 ** 3)
            return inner ** 3 - prev2 - prev1 ** 2"""

# 5-е по популярности решение
# Не нашёл

if __name__ == "__main__":
    print("main(3) ≈", main(3))
    print("main(9) ≈", main(9))
    print("main(8) ≈", main(8))
    print("main(4) ≈", main(4))
    print("main(6) ≈", main(6))
