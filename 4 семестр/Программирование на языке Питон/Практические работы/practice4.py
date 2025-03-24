def smalldet(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


A = [[4, 3], [1, 1]]
print("Задание 1:", smalldet(A))


def submatrix(A, i, j):
    a_len, b_len = len(A), len(A[0])
    submatrix = []
    for a in range(a_len):
        if a == i:
            continue
        line = []
        for b in range(b_len):
            if b == j:
                continue
            line.append(A[a][b])
        submatrix.append(line)
    return submatrix


A = [[0, 2, 1], [1, 4, 3], [2, 1, 1]]
print("Задание 2:", submatrix(A, 0, 0))


def det(A, i=0):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return smalldet(A)
    determinant = 0
    for j in range(n):
        determinant += (-1) ** (i + j) * A[i][j] * det(submatrix(A, i, j))
    return determinant


A = [[0, 2, 1, 4], [1, 0, 3, 2], [0, 1, 4, 0], [1, 2, 1, 1]]
print("Задание 3:", det(A))


def minor(A, i, j):
    return det(submatrix(A, i, j))


print("Задание 4:", minor(A, 0, 1))


def alg(A, i, j):
    return (-1) ** (i + j) * minor(A, i, j)


print("Задание 5:", alg(A, 1, 1))


def algmatrix(A):
    n = len(A)
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(alg(A, i, j))
        matrix.append(line)
    return matrix


print("Задание 6:", algmatrix(A))


def transpose(A):
    a_len, b_len = len(A), len(A[0])
    matrix = [[0] * b_len for _ in range(a_len)]
    for i in range(a_len):
        for j in range(b_len):
            matrix[j][i] = A[i][j]
    return matrix


def inv(A):
    n = len(A)
    det_A = det(A)
    if det_A == 0:
        raise ValueError("Детерминант равен нулю.")
    t_matrix = transpose(algmatrix(A))
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(t_matrix[i][j] / det_A)
        matrix.append(line)
    return matrix


print("Задание 7:", inv(A))


def multiply(A, B):
    m, n1 = len(A), len(A[0])
    n2, k = len(B), len(B[0])
    if n1 != n2:
        raise ValueError("Матрицы нельзя перемножить между собой.")
    matrix = [[0] * k for _ in range(m)]
    for i in range(m):
        for j in range(k):
            matrix[i][j] = sum(A[i][kk] * B[kk][j] for kk in range(n1))
    return matrix


def moore_penrose(H):
    H_T = transpose(H)
    return multiply(inv(multiply(H_T, H)), H_T)


print("Задание 8:", moore_penrose(A))
