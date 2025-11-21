#include <iostream>
#include <string>
#include <windows.h>
#include <cstdlib>
using namespace std;
#include <debugapi.h>

void make_memory_snapshot(const char* label) {
    OutputDebugStringA(label);
}

int length_of_matrix() {
    string m;
    while (true) {
        cout << "Введите целое значение M (количество строк и столбцов матрицы) в диапазоне [2, 5]\n";
        cout.width(8);
        cout << "Ввод: ";
        cin >> m;
        if (m == "2" || m == "3" || m == "4" || m == "5")
            break;
        else {
            cout << "Допущена ошибка! Вы должны вводить только целые числа из диапазона [2, 5]! Повторите попытку ввода!\n";
            m.clear();
        }
    }
    return stoi(m);
}

string answer_to_question() {
    string answer;
    while (true) {
        cout << "Вы хотите ввести данные в матрицу самостоятельно? (1/0)\n";
        cout.width(8);
        cout << "Ввод: ";
        cin >> answer;
        if (answer == "1" || answer == "0")
            break;
        else {
            cout << "Допущена ошибка! Вы должны ответить на вопрос только одним символом (1/0)! Повторите попытку ввода!\n";
            answer.clear();
        }
    }
    return answer;
}

int matrix_from_user(int* matrix, int M) {
    cout << "Далее Вам требуется вводить значения элементов в диапазоне [1, 100] (к примеру: A[1][0] = 5)\n";
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            string X;
            bool f = false;
            while (!f) {
                cout.width(5);
                cout << "A[" << i << "][" << j << "] = ";
                cin >> X;
                int l = X.length();
                bool p = true;
                for (int k = 0; k < l; k++) {
                    if (!isdigit(X[k])) {
                        cout << "Допущена ошибка! Вы должны вводить только целые числа из диапазона [1, 100]! Повторите попытку ввода!\n";
                        X.clear();
                        p = false;
                        break;
                    }
                }
                if (p) {
                    int x = stoi(X);
                    if (x >= 1 && x <= 100) {
                        *(matrix + i * M + j) = x;
                        f = true;
                    }
                    else {
                        cout << "Допущена ошибка! Вы должны вводить только целые числа из диапазона [1, 100]! Повторите попытку ввода!\n";
                        X.clear();
                    }
                }
            }
        }
    }
    return *matrix;
}

int matrix_from_random(int* matrix, int M) {
    srand(time(0));
    cout << "Массив будет заполнен случайными целыми числами в диапазоне [1, 100].\n";
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++)
            *(matrix + i * M + j) = rand() % 100 + 1;
    }
    return *matrix;
}

void cout_matrix(int* matrix, int M) {
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            cout.width(5);
            cout << *(matrix + i * M + j);
        }
        cout << endl;
    }
}

int matrix_sort(int* matrix, int M) {
    int* uninitialized_read = nullptr;
    if (M == 4 && uninitialized_read != nullptr) // Чтение неинициализированной памяти
        int value = *uninitialized_read;
    int k1 = ((M * M) - M) / 2 + M;
    int* m1 = new int[k1];
    int k2 = (M * M) - k1;
    int* m2 = new int[k2];
    k1 = 0;
    k2 = 0;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            if (i >= j) {
                m1[k1] = *(matrix + i * M + j);
                k1++;
            }
            else {
                m2[k2] = *(matrix + i * M + j);
                k2++;
            }
        }
    }
    int swap;
    for (int i = 0; i < k1; i++) {
        for (int j = i + 1; j < k1; j++) {
            if (m1[i] < m1[j]) {
                swap = m1[j];
                m1[j] = m1[i];
                m1[i] = swap;
            }
        }
    }
    k1 = 0;
    k2 = 0;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            if (i >= j) {
                *(matrix + i * M + j) = m1[k1];
                k1++;
            }
            else {
                *(matrix + i * M + j) = -m2[k2];
                k2++;
            }
        }
    }
    delete[] m1;
    delete[] m2;
    return *matrix;
}

void inefficient_algorithm(int* matrix, int M) {
    // Искусственная неэффективность
    for (int i = 0; i < M * 1000; i++)
        for (int j = 0; j < M * 1000; j++)
            volatile int dummy = i * j;
}

int main()
{
    setlocale(LC_ALL, "Russian");
    int M = length_of_matrix();
    string answer = answer_to_question();
    int* matrix = new int[M * M];
    make_memory_snapshot("После создания матрицы");
    if (M == 3) // Утечка при определённом входе
        int* conditional_leak = new int[500];
    if (answer == "1")
        *matrix = matrix_from_user(matrix, M);
    else
        *matrix = matrix_from_random(matrix, M);
    make_memory_snapshot("После заполнения матрицы");
    cout << "Полученная матрица:\n";
    cout_matrix(matrix, M);
    *matrix = matrix_sort(matrix, M);
    make_memory_snapshot("После сортировки");
    inefficient_algorithm(matrix, M); // Неэффективный алгоритм
    cout << "Итоговая матрица:\n";
    cout_matrix(matrix, M);
    delete[] matrix;
    make_memory_snapshot("Перед завершением");
    return 0;
}
