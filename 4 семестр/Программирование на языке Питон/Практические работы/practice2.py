print("\nЗадание 1")


def f(n, m, a):
    res = 1
    for c in range(1, a + 1):
        mult = 1
        for j in range(1, m + 1):
            sum = 0
            for i in range(1, n + 1):
                sum += (28 * c ** 2) ** 6 / 5 + 16 * (j ** 3 / 44 + i ** 2) ** 5
            mult *= sum
        res *= mult
    return res


print(f(4, 2, 8))

print("\nЗадание 2")


def d1(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += (y[i - 1] - z[i - 1]) ** 2
    return sum ** 0.5


y, z = (1, 0.5, 1), (0.5, 2, 1)
print(d1(y, z))

print("\nЗадание 3")


def d2(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += abs(y[i - 1] - z[i - 1])
    return sum


print(d2(y, z))

print("\nЗадание 4")


def d3(y, z):
    n = len(y)
    max = -1
    for i in range(1, n + 1):
        if max < abs(y[i - 1] - z[i - 1]):
            max = abs(y[i - 1] - z[i - 1])
    return max


print(d3(y, z))

print("\nЗадание 5")


def d4(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += (y[i - 1] - z[i - 1]) ** 2
    return sum


print(d4(y, z))

print("\nЗадание 6")


def d5(y, z):
    n = len(y)
    sum = 0
    h = 5
    for i in range(1, n + 1):
        sum += abs(y[i - 1] - z[i - 1]) ** h
    return sum ** (1 / h)


print(d5(y, z))

print("\nЗадание 7")
import matplotlib.pyplot as plt


def visualize(distance_metrics, y, z, move=1.0):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = plt.subplots()
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])
    plt.show()


list = (d1, d2, d3, d4, d5)
visualize(list, y, z, 1.5)

print("\nЗадание 8")
words = ["language!", "programming", "Python", "the", "love", "I"]

message = " ".join(words[::-1])
print(message)

print("\nЗадание 9")


def f(s, c):
    return s.lower().count(c)


def count_characters(string):
    new_string = string.lower().replace(' ', '')
    dictionary = {}
    for char in new_string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


print(count_characters(message))

print("\nЗадание 10")


def f(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    if a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    return 1 + min(f(a, b, i, j - 1), f(a, b, i - 1, j), f(a, b, i - 1, j - 1))


a1, b1 = "Hello, world!", "Goodbye, world!"
a2, b2 = "Hello, world!", "Bye, world!"
a3, b3 = "I love Python", "I like Python"
a4, b4 = "100101", "100011"
print(f(a1, b1, len(a1), len(b1)))
print(f(a2, b2, len(a2), len(b2)))
print(f(a3, b3, len(a3), len(b3)))
print(f(a4, b4, len(a4), len(b4)))

print("\nЗадание 11")
import timeit
from Levenshtein import distance as levenshtein_distance_c


def Levenshtein_distance_python(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[len(a)][len(b)]


print("\nPython:")
print(timeit.timeit(lambda: Levenshtein_distance_python(a1, b1), number=1000))
print(timeit.timeit(lambda: Levenshtein_distance_python(a2, b2), number=1000))
print(timeit.timeit(lambda: Levenshtein_distance_python(a3, b3), number=1000))
print(timeit.timeit(lambda: Levenshtein_distance_python(a4, b4), number=1000))

print("\nC:")
print(timeit.timeit(lambda: levenshtein_distance_c(a1, b1), number=1000))
print(timeit.timeit(lambda: levenshtein_distance_c(a2, b2), number=1000))
print(timeit.timeit(lambda: levenshtein_distance_c(a3, b3), number=1000))
print(timeit.timeit(lambda: levenshtein_distance_c(a4, b4), number=1000))
