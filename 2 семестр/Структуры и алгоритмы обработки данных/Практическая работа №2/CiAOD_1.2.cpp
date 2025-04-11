#include <iostream>
#include <ctime>

using namespace std;

void print_array(int* array, int n) {
    for (int i = 0; i < n; i++) {
        cout << array[i];
        if (i != n - 1)
            cout << ' ';
    }
    cout << endl;
}
long long Insertion_sort(int* array, int n) {
    long long Cp = 0, Mp = 0;
    for (int i = 1; i < n; i++) {
        Cp++;
        int key = array[i];
        Mp++;
        int j = i - 1;
        Mp++;
        while (j >= 0 && array[j] > key) {
            Cp += 2;
            array[j + 1] = array[j]; 
            Mp++;
            j--; 
            Mp++;
        }
        Cp++;
        array[j + 1] = key; 
        Mp++;
    }
    Cp++;
    return (Cp + Mp);
}
long long Selection_sort(int* array, int n) {
    long long Cp = 0, Mp = 0; 
    for (int i = 0; i < n - 1; i++) {
        Cp++;
        int min_idx = i;
        Mp++;
        for (int j = i + 1; j < n; j++) {
            Cp++;
            if (array[j] < array[min_idx]) {
                min_idx = j;
                Mp++;
            }
            Cp++;
        }
        Cp++;
        if (min_idx != i) {
            swap(array[min_idx], array[i]);
            Mp += 3;
        }
        Cp++;
    }
    Cp++;
    return (Cp + Mp);
}

int main()
{
    setlocale(LC_ALL, "RUS");
    cout << "Введите n: "; int n; cin >> n;
    srand(time(0));
    int* array = new int[n];
    for (int i = 0; i < n; i++)
        array[i] = rand() % 101;
    cout << "\nНеотсортированный массив:\n";
    print_array(array, n);
    unsigned int start_time = clock();
    long long count = Selection_sort(array, n);
    unsigned int end_time = clock();
    cout << "\nОтсортированный массив:\n";
    print_array(array, n);
    cout << endl;
    cout << "Время работы составило " << end_time - start_time << "мс.\n";
    cout << "Фактическое количество фактических операций составило " << count << ".\n";
    return 0;
}