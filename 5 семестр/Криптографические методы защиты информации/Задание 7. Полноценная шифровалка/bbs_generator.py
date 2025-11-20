import random
import math

def is_prime_miller_rabin(n, k=10):
    if n == 2 or n == 3: return True
    if n <= 1 or n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0: r += 1; d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def generate_prime():
    while True:
        num = random.getrandbits(50)
        if num >= 2**49 and num % 4 == 3 and is_prime_miller_rabin(num):
            return num

def bbs_generator(length, p=None, q=None, X=None):
    p = p or generate_prime()
    q = q or generate_prime()
    while p == q: q = generate_prime()
    N = p * q
    if X is None:
        X = random.randint(2, N - 1)
        while math.gcd(X, N) != 1: X = random.randint(2, N - 1)
    gamma, X_i = [], (X ** 2) % N
    for _ in range(length):
        X_i = (X_i ** 2) % N
        gamma.append(str(X_i % 2))
    return "".join(gamma), p, q, X

if __name__ == '__main__':
    gamma, p, q, X = bbs_generator(10000)
    print(f"Гамма: {gamma[:100]}...")
    print(f"Параметры: p={p}, q={q}, X={X}")
