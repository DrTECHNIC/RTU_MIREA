#include <cstdlib>
#include <iostream>
#include <Windows.h>
#include <bitset>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <set>

using namespace std;

void ciaod_1a()
{
	unsigned char x = 255;			//8-разрядное двоичное число 11111111
	unsigned char maska = 1;		//1=00000001 – 8-разрядная маска
	cout << (x & (~(maska << 4)));	//результат x=239
}

void ciaod_1b()
{
	unsigned char x = 128;			//8-разрядное двоичное число 10000000
	unsigned char maska = 1;		//1=00000001 – 8-разрядная маска
	cout << (x | (maska << 6));		//результат x=192
}

void ciaod_1v()
{
	unsigned int x = 25;
	const int n = sizeof(int) * 8; //=32 - количетсво разрядов в числе типа int
	unsigned maska = (1 << n - 1); //1 в старшем бите 32-разрядной сетки
    cout << "Начальный вид маски: " << bitset<n>(maska) << endl;
    cout << "Результат: ";
    for (int i = 1; i <= n; i++) //32 раза - по количеству разрядов:
    {
        cout << ((x & maska) >> (n - i));
        maska = maska >> 1; //смещение 1 в маске на разряд вправо
    }
    cout << endl;
    system("pause");
}

void ciaod_2a()
{
    cout << "Введите число от 1 до 8 (разряд массива): ";
    int n; cin >> n;
    cout << "Вводите числа из диапазона от 0 до 7.\n";
    int* array = new int[n]; //создание динамического массива для хранения в нем вводимых чисел
    for (int i = 0; i < n; i++) //ввод чисел
    {
        int num; cin >> num;
        array[i] = num;
    }
    unsigned char bit_mas = 0; //создание массива из битов
    for (int i = 0; i < n; i++) //заполнение этого массива
    {
        unsigned char maska = 1;
        maska = (maska << array[i]);
        bit_mas = bit_mas | maska;
    }
    for (int i = 0; i < 8; i++) //вывод на экран отсортированного списка чисел
    {
        if ((bit_mas & 1) == 1)
            cout << i << ' ';
        bit_mas >>= 1;
    }
}

void ciaod_2b()
{
    cout << "Введите число от 1 до 64 (разряд массива): ";
    int n; cin >> n;
    cout << "Вводите числа из диапазона от 0 до 63.\n";
    int* array = new int[n]; //создание динамического массива для хранения в нем вводимых чисел
    for (int i = 0; i < n; i++) //ввод чисел
    {
        int num; cin >> num;
        array[i] = num;
    }
    unsigned long long int bit_mas = 0; //создание массива из битов
    for (int i = 0; i < n; i++) //заполнение этого массива
    {
        unsigned long long int maska = 1;
        maska = (maska << array[i]);
        bit_mas = bit_mas | maska;
    }
    for (int i = 0; i < sizeof(bit_mas) * 8; i++) //вывод на экран отсортированного списка чисел
    {
        if ((bit_mas & 1) == 1)
            cout << i << ' ';
        bit_mas >>= 1;
    }
}

void ciaod_2v()
{
    cout << "Введите число от 1 до 64 (разряд массива): ";
    int n; cin >> n;
    cout << "Вводите числа из диапазона от 0 до 63.\n";
    vector<unsigned char> array(8); //создание массива для хранения данных в битовом формате
    unsigned char maska = 1;
    for (int i = 0; i < n; i++) //ввод чисел
    {
        int num; cin >> num;
        array[num / 8] = array[num / 8] | (maska << num % 8);
    }
    for (int i = 0; i < 8; i++) //вывод на экран отсортированного списка чисел
        for (int j = 0; j < 8; j++)
        {
            if ((array[i] & 1) == 1)
                cout << 8 * i + j << ' ';
            array[i] >>= 1;
        }
}

void create_file()
{
    const long n = 1000000; //минимальное значение чисел
    const long n_max = 9999999; //максимальное значение чисел
    const long length = n_max - n + 1; //максимальное количество чисел
    long* array = new long[length]; //динамический массив для хранения чисел
    for (long i = 0; i < length; i++) //заполнение массива числами
        array[i] = n + i;
    srand(time(NULL));
    for (long i = 0; i < length; i++) //перемешивание чисел в массиве
        swap(array[i], array[rand() % length]);
    ofstream file_out("test.txt");
    for (int i = 0; i < length; i++) //занесение чисел в файл
        file_out << array[i] << endl;
    file_out.close();
}
void ciaod_3()
{
    create_file();
    const int n = 10000000 / 8;
    int start = clock(); //запуск таймера
    unsigned char maska = 1;
    vector<unsigned char> bit_array(n); //создание битового массива размера n строк
    ifstream file_in("test.txt");
    int character;
    while (!file_in.eof()) //считывание данных из файла
    {
        file_in >> character;
        bit_array[character / 8] = bit_array[character / 8] | (maska << character % 8);
    }
    file_in.close();
    int stop = clock(); //остановка таймера
    ofstream file_out("test.txt");
    for (int i = 0; i < n; i++) //вывод чисел на экран
        for (int j = 0; j < 8; j++)
        {
            if ((bit_array[i] & 1) == 1)
                file_out << 8 * i + j << endl;
            bit_array[i] >>= 1;
        }
    file_out.close();
    int work_time = stop - start; //время работы
    bit_array.shrink_to_fit();
    cout << bit_array.capacity() << " b\n" << bit_array.capacity() / 1024 << " kb\n"
        << bit_array.capacity() / (1024 * 1024) << " mb\nTime: " << work_time << "ms";
}

struct Product
{
	string name;
	int code;
};
bool read_product_from_file(ifstream& file, int index, Product& product) 
{
    file.clear(); //сбрасываем флаги потока
    file.seekg(0, ios::beg); //возвращаем указатель чтения в начало файла
    string line; int current_line = 0;
    while (getline(file, line)) //читаем строки до нужной
    {
        if (current_line == index) 
        {
            size_t comma_pos = line.find(',');
            if (comma_pos != string::npos) 
            {
                product.name = line.substr(0, comma_pos);
                product.code = stoi(line.substr(comma_pos + 1));
                return true; //успешно считали продукт
            }
        }
        current_line++;
    }
    return false; //если не удалось найти нужную строку
}
bool binary_homogeneous_search_without_using_an_additional_table(const string& binary_file, int total_lines, int search_code, Product& found_product)
{
    ifstream file(binary_file);
    int left = 0, right = total_lines - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2; //определение центра относительно знаечний переменных left и right
        Product product;
        if (read_product_from_file(file, mid, product)) //читаем продукт с позиции mid
        {
            if (product.code == search_code) //элемент найден
            {
                found_product = product;
                return true;
            }
            else if (product.code > search_code) //ищем в левой половине
                right = mid - 1;
            else //ищем в правой половине
                left = mid + 1;
        }
        else return false;
    }
    return false; //продукт не найден
}
void ciaod_4b()
{
    cout << "Введите код для поиска: ";
    int search_code; cin >> search_code;
    string binary_file = "1000.bin"; int total_lines = 1000; Product found_product;
    int start = clock(); //запуск таймера
    if (binary_homogeneous_search_without_using_an_additional_table(binary_file, total_lines, search_code, found_product))
        cout << "Товар найден: " << found_product.name << ", код: " << found_product.code;
    else
        cout << "Товар с кодом " << search_code << " не найден.";
    int end = clock(); //остановка таймера
    cout << endl << "Время работы: " << end - start << " мс."; //вывод на экран времени работы
}

struct index_entry
{
    int code;
    streampos pos;
};
vector<index_entry> build_index_table(string filename)
{
    ifstream file(filename);
    vector<index_entry> index_table;
    string line; streampos position;
    while (file) //проходим по файлу и сохраняем код продукта и его смещение
    {
        position = file.tellg(); //запоминаем позицию перед чтением строки
        if (!getline(file, line))
            break;
        size_t comma_pos = line.find(','); //нахождение координат запятой в строке
        if (comma_pos != string::npos)
        {
            int code = stoi(line.substr(comma_pos + 1));
            index_table.push_back({ code, position });
        }
    }
    file.close();
    return index_table;
}
streampos find_in_table(const vector<index_entry>& index_table, int target_code)
{
    for (const auto& entry : index_table)
        if (entry.code == target_code) 
            return entry.pos;
    return -1; //если код не найден
}
Product read_product_by_position(string filename, streampos pos)
{
    ifstream file(filename);
    file.seekg(pos); //перемещение указателя в файле на позицию pos
    string line; getline(file, line);
    size_t comma_pos = line.find(','); //нахождение координат запятой в строке
    string name = line.substr(0, comma_pos);
    int code = stoi(line.substr(comma_pos + 1));
    file.close();
    return { name, code };
}
void ciaod_4v()
{
    string binary_file = "10000.bin"; vector<index_entry> index_table;
    index_table = build_index_table(binary_file);
    Product found_product;
    cout << "Введите код для поиска: ";
    int search_code; cin >> search_code;
    int start = clock(); //запуск таймера
    streampos pos = find_in_table(index_table, search_code);
    int end = clock(); //остановка таймера
    if (pos != -1)
    {
        Product found_product = read_product_by_position(binary_file, pos); //нахождение продукта с заданным кодом
        cout << "Товар найден: " << found_product.name << ", код: " << found_product.code;
    }
    else
        cout << "Товар с кодом " << search_code << " не найден.";
    cout << endl << "Время работы: " << end - start << " мс."; //вывод на экран времени работы
}

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
	ciaod_4v();
	return 0;
}