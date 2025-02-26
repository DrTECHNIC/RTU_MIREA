# Задание 3
def prac3_1():
    s = ["1", "2", "3"]
    print([int(i) for i in s])


def prac3_2():
    s = [1, 2, 2, 3, 3, 3]
    print(len(set(s)))


def prac3_3():
    s = [1, 2, 3, 4]
    print(s[::-1])


def prac3_4():
    s = [1, 3, 4, 5, 6, 4]
    x = 4
    print([i for i, val in enumerate(s) if val == x])


def prac3_5():
    s = [1, 2, 3, 4, 5, 7]
    print(sum(s[i] for i in range(0, len(s), 2)))


def prac3_6():
    s = ["12345", "qwerty", "wasd"]
    print(max(s, key=len))


def prac3_7():
    x = 24
    print(x % sum(map(int, str(x))) == 0)


def prac3_8():
    from itertools import groupby

    s = 'ABBCCCDEF'
    print([(k, len(list(g))) for k, g in groupby(s)])
    print([(k, sum(1 for _ in g)) for k, g in groupby(s)])


# Задание 4
def task4_1():
    A = [[0, 2], [3, 0]]
    B = [[1, 4], [2, 0]]

    def multiply(A, B):
        C = []
        for n in range(len(A)):
            ap = []
            for m in range(len(A[n])):
                ap.append(A[n][m] * B[n][m])
            C.append(ap)
        return C

    print(multiply(A, B))


def task4_2():
    A = [[0, 2, 1], [1, 0, 3], [0, 1, 1]]

    def transpose(A):
        C = []
        for n in range(len(A)):
            ap = []
            for m in range(len(A[n])):
                ap.append(A[m][n])
            C.append(ap)
        return C

    print(transpose(A))


def task4_3():
    A = [[1, 2], [3, 4], [5, 6]]
    B = [[1, 2, 3], [4, 5, 6]]

    def dot(A, B):
        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    print(dot(A, B))


# Задание 5
def task5_1():
    def generate_groups():
        array = []
        groups = ["ИВБО", "ИКБО", "ИМБО", "ИНБО"]
        for group in groups:
            if group == "ИВБО":
                append = []
                numbers = [10, 11, 12, 13, 20, 21, 22]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append(append)

            elif group == "ИКБО":
                append = []
                numbers = [10, 10, 11, 12, 13, 14, 15, 20, 21, 22, 24, 34,
                           40, 41, 42, 43, 50, 51, 52, 60, 61, 62, 63, 64,
                           65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76]
                flag = 1
                for number in numbers:
                    if number == 10 and flag == 1 or number == 24 or number == 34:
                        append.append(group + '-' + str(number) + "-22")
                        flag = 0
                    else:
                        append.append(group + '-' + str(number) + "-23")
                array.append(append)

            elif group == "ИМБО":
                append = []
                numbers = [10, 11]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append(append)

            elif group == "ИНБО":
                append = []
                numbers = [10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append(append)

        return array

    list_of_groups = generate_groups()
    for i in list_of_groups:
        print('\n' + i[0][0:4] + ':')
        count = 0
        for j in i:
            print(j, end=" ")
            count += 1
            if count == 10:
                count = 0
                print()
        print()


def task5_2():
    import sys

    def Daniil_print(*objects, sep=' ', end='\n', file=sys.stdout):
        arg = [str(i) for i in objects]
        text = sep.join(arg) + end
        file.write(text)

    Daniil_print(123, "456")


def task5_3():
    def decrypt(v: list[2], k: list[4]):
        v0 = v[0]
        v1 = v[1]
        sum = 0xC6EF3720
        delta = 0x9E3779B9
        k0 = k[0]
        k1 = k[1]
        k2 = k[2]
        k3 = k[3]
        for i in range(32):
            v1.value -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3)
            v0.value -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1)
            sum -= delta
        v[0] = v0
        v[1] = v1


if __name__ == "__main__":
    task5_3()
