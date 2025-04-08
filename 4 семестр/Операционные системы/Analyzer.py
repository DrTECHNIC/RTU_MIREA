import numpy as np
import argparse


def detect_deadlock(T, C, R):
    m = len(T)
    n = len(C)

    if C.shape != (n, m) or R.shape != (n, m):
        raise ValueError("Несоответствие размеров матриц C и R вектору T")

    if np.any(T < 0) or np.any(C < 0) or np.any(R < 0):
        raise ValueError("Все значения в T, C и R должны быть неотрицательными")

    max_per_column = np.max(C, axis=0)
    if np.any(max_per_column > T):
        raise ValueError(f"Недостаточно ресурсов")

    A = np.array(T) - np.sum(C, axis=0)
    completed = np.zeros(n, dtype=bool)

    while True:
        found = False
        for i in range(n):
            if not completed[i] and np.all(R[i] <= A):
                A += C[i]
                completed[i] = True
                found = True

        if not found:
            break

    if np.any(~completed):
        print("Обнаружена взаимоблокировка")
    else:
        print("Взаимоблокировка не обнаружена")


def read_vector(name):
    with open(name) as file:
        return np.array(list(map(int, file.readline().strip().split())))


def read_matrix(name):
    with open(name) as file:
        return np.array([list(map(int, line.strip().split())) for line in file])


def main():
    parser = argparse.ArgumentParser(description="Анализатор взаимоблокировок ресурсов")
    parser.add_argument('file_T', type=str, help="Файл с общими ресурсами (T)")
    parser.add_argument('file_C', type=str, help="Файл с матрицей текущих выделений (C)")
    parser.add_argument('file_R', type=str, help="Файл с матрицей запросов (R)")
    args = parser.parse_args()

    try:
        T = read_vector(args.file_T)
        C = read_matrix(args.file_C)
        R = read_matrix(args.file_R)

        detect_deadlock(T, C, R)

    except ValueError as ve:
        print(f"Ошибка данных: {ve}")
    except FileNotFoundError as fe:
        print(f"Ошибка файла: {fe}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
