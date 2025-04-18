# Самое популярное решение
"""def main(y, z):
    sum = 0
    n = len(y)
    for i in range(1, n + 1):
        sum += 65 * (56 * z[i - 1] - y[n - i] ** 3 - 61 * z[n - i] ** 2) ** 5
    return sum"""


# 2-е по популярности решение
"""def main(y, z):
    n = len(y)
    return sum(65 * (56 * z[i - 1] - y[n - i] ** 3 -
                     61 * z[n - i] ** 2) ** 5 for i in range(1, n + 1))"""


# 3-е по популярности решение
"""def main(y, z):
    n = len(y)
    i = 0
    sum = 0
    while i < n:
        i += 1
        sum += 65 * (56 * z[i - 1] - y[n - i] ** 3 - 61 * z[n - i] ** 2) ** 5
    return sum"""


# 4-е по популярности решение
"""def main(y, z, i=0):
    if i == len(y):
        return 0
    term = 56 * z[i] - y[len(y) - 1 - i] ** 3 - 61 * z[len(z) - 1 - i] ** 2
    return 65 * (term ** 5) + main(y, z, i + 1)"""


if __name__ == "__main__":
    print("main([-0.69, -0.74, 0.7, -0.33, -0.4, 0.92], [0.12, 0.82, 0.58, -0.6, -0.06, 0.77]) ≈",
          main([-0.69, -0.74, 0.7, -0.33, -0.4, 0.92], [0.12, 0.82, 0.58, -0.6, -0.06, 0.77]))
    print("main([-0.79, -0.91, -0.61, 0.17, 1.0, -0.87], [0.3, -0.29, -0.74, 0.59, 0.78, -0.6]) ≈",
          main([-0.79, -0.91, -0.61, 0.17, 1.0, -0.87], [0.3, -0.29, -0.74, 0.59, 0.78, -0.6]))
    print("main([0.84, 0.45, -0.68, -0.93, -0.78, -0.61], [0.45, -0.79, 0.18, 0.88, 0.33, 0.71]) ≈",
          main([0.84, 0.45, -0.68, -0.93, -0.78, -0.61], [0.45, -0.79, 0.18, 0.88, 0.33, 0.71]))
    print("main([0.68, 0.54, -0.83, 0.71, -0.47, 0.43], [0.87, 0.9, -0.33, 0.68, -0.64, 0.29]) ≈",
          main([0.68, 0.54, -0.83, 0.71, -0.47, 0.43], [0.87, 0.9, -0.33, 0.68, -0.64, 0.29]))
    print("main([0.82, -0.52, -0.71, 0.51, -0.28, 0.81], [-0.62, 0.81, -0.49, -0.39, -0.55, -0.43]) ≈",
          main([0.82, -0.52, -0.71, 0.51, -0.28, 0.81], [-0.62, 0.81, -0.49, -0.39, -0.55, -0.43]))
