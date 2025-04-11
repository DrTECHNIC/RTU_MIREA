#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <Windows.h>

using namespace std;

void ciaod_6_1();
void ciaod_6_2_1();
void ciaod_6_2_2();

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    ciaod_6_2_2(); // ciaod_6_1() / ciaod_6_2_1() / ciaod_6_2_2()
    return 0;
}

struct Data
{
    string code; // Код специальности
    string name; // Название ВУЗа
};

class HashTable
{

private:

    vector<Data*> table; // Хеш-таблица
    int count; // Кол-во элементов в таблице

public:

    HashTable() // Конструктор хеш-таблицы
    {
        count = 0; table.resize(10, nullptr);
        ifstream file;
        file.open("text.txt");
        Data* element = new Data();
        for (int i = 0; i < 7; i++) // Начальное заполненние таблицы
        {
            file >> element->code >> element->name;
            Input(element);
            element = new Data();;
        }
        delete element;
        file.close();
    }

    void Input(Data* element) // Функция для ввода данных в таблицу
    {
        int code = Format(element->code, table.size()); // Определение хеша элемента
        int i = 0, index = code;
        // Цикл будет выполняться до тех пор, пока для элемента не найдется свободное место
        while (true) 
        {
            // Если таблица заполнена, то выполняем рехеширование
            if ((index + 7 * i) > (table.size() - 1)) 
            {
                Rehash(); continue;
            }
            // Если на данном месте уже есть элемент, то...
            if (table[index + 7 * i]) 
            {
                // Если коды элементов одинаковые, то изменяем название ВУЗа
                if (table[index + 7 * i]->code == element->code)
                {
                    table[index + 7 * i]->name = element->name;
                    ++count; delete element; break;
                }
                ++i; continue;
            }
            // Присваивание элементу таблицы значения кода специальности и названия ВУЗа
            table[index + 7 * i] = element; ++count; break;
        }
        // Выполняем рехеширование в случае необходимости
        if ((double)count / table.size() >= 0.75) Rehash();
    }

    void Delete(string code) // Функция для удаления элемента из таблицы
    {
        int index = Format(code, table.size()); // Определение хеша элемента
        // Поиск элемента в таблице по коду специальности
        for (int i = index; i < table.size(); i += 7)
            if (table[i]->code == code)
            {
                Data* element = table[i];
                table[i] = nullptr;
                delete element; return;
            }
    }

    Data* Search(string code) // Функция для поиск элемента в таблице
    {
        int index = Format(code, table.size()); // Определение хеша элемента
        // Поиск элемента в таблице по коду специальности
        for (int i = index; i < table.size(); i += 7)
            if (table[i]->code == code)
                return table[i];
        return nullptr;
    }

    void Print() // Функция для вывода таблицы на экран
    {
        // В случае, если элемент таблицы не nullptr, выводим его на экран
        for (Data* element : table) if (element)
            cout << element->code << ' ' << element->name << '\n';
    }

    int Format(string code, int dl) // Функция для определения индекса элемента таблицы
    {
        int cd = 0;
        for (int i = 0; i < code.length(); i++)
            cd += code[i];
        return cd % dl;
    }

    void Rehash() // Функция для рехеширования таблицы
    {
        bool flag = false;
        vector<Data*> Vector; // Объявление новой хеш-таблицы
        for (int i = 2; !flag; i *= 2)
        {
            Vector.resize(0); Vector.resize(table.size() * i, nullptr); flag = true;
            // Занесение данных из старой хеш-таблицы в новую
            for (Data* element : table)
            {
                if (element)
                {
                    int code = Format(element->code, Vector.size());
                    if (code > Vector.size() - 1)
                    {
                        flag = false; break;
                    }
                    Vector[code] = element;
                }
            }
        }
        // Изменение старой хеш-таблицы на новую
        table = Vector;
    }
};

void ciaod_6_1()
{
    HashTable hash_table = HashTable();
    cout << "Элементы хеш-таблицы:\n";
    hash_table.Print();
    while (true)
    {
        cout << "\nВыберите одну из функций:\n1 - Вывод содержимого;\n"
            << "2 - Добавление записи;\n3 - Удаление записи;\n"
            << "4 - Поиск записи;\n0 - Выход.\nНомер действия: ";
        int choice; cin >> choice;
        if (choice == 1)
        {
            cout << "\nЭлементы хеш-таблицы:\n";
            hash_table.Print();
            continue;
        }
        else if (choice == 2)
        {
            cout << "\nВведите данные новой записи: ";
            Data* element = new Data();
            cin >> element->code >> element->name;
            hash_table.Input(element);
            delete element;
            continue;
        }
        else if (choice == 3)
        {
            cout << "\nВведите код записи для удаления: ";
            string code; cin >> code; hash_table.Delete(code);
            continue;
        }
        else if (choice == 4)
        {
            cout << "\nВведите код записи для поиска: ";
            string code; cin >> code;
            Data* element = new Data();
            element = hash_table.Search(code);
            if (element) cout << "Найденная запись: " << element->code << ' ' << element->name << '\n';
            else cout << "Запись с кодом " << code << " не найдена.\n";
            delete element;
            continue;
        }
        else if (choice == 0)
            return;
        else
        {
            cout << "\nДопущена ошибка в выборе функции.\nПовторите попытку ввода.";
            continue;
        }
    }
}

string Replace(string str) // Функция для замены знаков на пробелы
{
    string new_str = ""; // Новая строка
    string end = "!?."; // Знаки между предложениями
    string between = ",;:-\"()/\\«»—[]"; // Знаки между словами
    bool flag = false; // Флаг для запоминания "состояния" пробелов
    for (int i = 0; i < str.length(); ++i) // Проход по встроке
    {
        // Проверка на русскую букву
        if (str[i] >= 'а' && str[i] <= 'я' || str[i] >= 'А' && str[i] <= 'Я' || str[i] == 'ё' || str[i] == 'Ё')
        {
            if (flag) flag = false;
            new_str += str[i];
        }
        // Проверка на пробел
        else if (str[i] == ' ' && !flag)
        {
            new_str += ' ';
            flag = true;
        }
        else
            // Проверка на символ между словами
            if (between.find(str[i]) != string::npos)
            {
                if (!flag)
                {
                    new_str += ' ';
                    flag = true;
                }
            }
            // Проверка на символ между предложениями
            else if (end.find(str[i]) != string::npos)
            {
                if (!flag)
                {
                    new_str += "  ";
                    flag = true;
                }
            }
    }
    return new_str; // Вовзрат новой строки
}

void ciaod_6_2_1()
{
    string text = "";
    text += "На рассвете мы отправились в лес — аромат свежести и хвои наполнял воздух. Вдруг, среди деревьев, мы заметили: дикие цветы, искрящиеся росой, привлекли наше внимание.";
    text += "\"Как красиво!\" — воскликнула Мария, указывая на ярко-красные маки. Мы решили остановиться, чтобы сделать несколько фотографий. В тишине слышался лишь шёпот листьев ";
    text += "и пение птиц, словно лес приглашал нас в своё волшебное царство.";
    cout << "\nИсходный текст:\n" << text << "\nИзмененный текст:\n" << Replace(text) << endl;
}

vector<int> PrefixFunction(string s) // Функция для поиска префикс функции
{
    int n = s.length();
    vector<int> pi(n); // Создание вектора для значений префикс функции
    for (int i = 1; i < n; ++i) // Заполнение вектора
    {
        int cur = pi[i - 1];
        while (cur > 0 && s[i] != s[cur])
            cur = pi[cur - 1];
        if (s[i] == s[cur])
            ++cur;
        pi[i] = cur;
    }
    return pi; // Вовзрат значения вектора
}

void ciaod_6_2_2()
{
    string S = "good morning, i want to say google";
    cout << "Исходная строка:\n" << S;
    vector<int> pi = PrefixFunction(S);
    cout << "\n\nПрефикс-функция для строки:\n[ ";
    for (size_t i = 0; i < pi.size(); ++i)
    {
        cout << pi[i];
        if (i != pi.size() - 1)
            cout << ',';
        cout << ' ';
    }
    cout << ']';
}