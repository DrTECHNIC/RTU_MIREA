#include <iostream>
#include <ctime>
using namespace std;

void Print_Array(int* arr, int n)
{
    cout << endl << arr[0];
    for (int i = 1; i < n; i++)
        cout << ' ' << arr[i];
    cout << endl;
}

void Cocktail_Sort(int* arr, int size)
{
    int control = size - 1;
    int left = 0, right = control;
    while (left < right) 
    {
        for (int i = left; i < right; i++) 
            if (arr[i] > arr[i + 1]) 
            {
                swap(arr[i], arr[i + 1]);
                control = i;
            }
        right = control;
        for (int i = right; i > left; i--) 
            if (arr[i] < arr[i - 1]) 
            {
                swap(arr[i], arr[i - 1]);
                control = i;
            }
        left = control;
    }
}

void Quick_Sort(int* arr, int low, int high)
{
    if (low < high)
    {
        int pivot = arr[(low + high) / 2];
        int i = low;
        int j = high;
        while (i <= j)
        {
            while (arr[i] < pivot)
                i++;
            while (arr[j] > pivot)
                j--;
            if (i <= j)
            {
                swap(arr[i], arr[j]);
                i++;
                j--;
            }
        }
        Quick_Sort(arr, low, j);
        Quick_Sort(arr, i, high);
    }
}

int main()
{
    cout << "Array's size: "; int size; cin >> size; cout << endl;
    srand(time(0));
    int* arr = new int[size];
    for (int i = 0; i < size; i++)
    {
        arr[i] = rand() % 101;
        //arr[i] = i;
        //arr[i] = size - i;
    }
    //cout << "\nUnsorted array:"; Print_Array(arr, size);
    int start_time = clock();
    Cocktail_Sort(arr, size);
    //Quick_Sort(arr, 0, size - 1);
    int end_time = clock();
    cout << endl << "Work time: " << end_time - start_time << endl;
    //cout << "\nSorted array:"; Print_Array(arr, size);
}