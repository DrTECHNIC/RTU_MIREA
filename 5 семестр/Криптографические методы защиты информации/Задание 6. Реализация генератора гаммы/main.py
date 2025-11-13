import random
import math

def is_prime_miller_rabin(n, k=10):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime():
    while True:
        num = random.getrandbits(50)
        if num < 2 ** 49:
            continue
        if num % 4 == 3 and is_prime_miller_rabin(num):
            return num

def bbs_generator(length):
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()
    N = p * q
    X = 2 ** 40
    while math.gcd(X, N) != 1:
        X = random.randint(2, N - 1)
    gamma = []
    X_i = (X ** 2) % N
    for _ in range(length):
        X_i = (X_i ** 2) % N
        gamma.append(str(X_i % 2))
    return "".join(gamma)

def check_n_grams(sequence, n):
    n_grams = [sequence[i:i + n] for i in range(0, len(sequence) - n + 1)]
    n_gram_counts = {}
    for gram in n_grams:
        n_gram_counts[gram] = n_gram_counts.get(gram, 0) + 1
    total = len(n_grams)
    expected = total / (2 ** n)
    print(f"\n{n}-граммы (всего {len(n_gram_counts)} различных):")
    for gram, count in sorted(n_gram_counts.items()):
        percentage = count / total * 100
        print(f"  {gram}: {count} ({percentage:.2f}%)")
    max_count = max(n_gram_counts.values())
    min_count = min(n_gram_counts.values())
    deviation = abs(max_count - min_count) / expected * 100
    return deviation

def check_golomb_postulates(sequence):
    total = len(sequence)
    zeros = sequence.count('0')
    ones = sequence.count('1')
    print(f"Количество нулей: {zeros} ({zeros / total * 100:.2f}%)")
    print(f"Количество единиц: {ones} ({ones / total * 100:.2f}%)")
    max_deviations = []
    for n in range(2, 11):
        deviation = check_n_grams(sequence, n)
        max_deviations.append(deviation)
        if n > 4:
            expected_grams = min(2 ** n, total - n + 1)
            actual_grams = len(set(sequence[i:i + n] for i in range(0, total - n + 1)))
            coverage = actual_grams / expected_grams * 100
            print(f"Покрытие различных {n}-грамм: {coverage:.2f}%")

def main():
    gamma = bbs_generator(10000)
    print(gamma)

    check_golomb_postulates(gamma)

if __name__ == '__main__':
    main()
