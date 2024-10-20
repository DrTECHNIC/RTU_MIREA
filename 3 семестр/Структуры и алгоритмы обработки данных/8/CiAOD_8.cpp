#include "Windows.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <random>
#include <cmath>

using namespace std;

void ciaod_8_1();
void ciaod_8_2();

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    ciaod_8_2(); // ciaod_8_1() / ciaod_8_2()
    return 0;
}

struct let
{
    char lt;
    int cnt;
    let(char lt, int cnt)
    {
        this->lt = lt;
        this->cnt = cnt;
    }
};

bool compare_lets(const let* pr1, const let* pr2)
{ return pr1->cnt > pr2->cnt; }

void rec(int st, int fn, int sm[], map<char, string>& codes, vector<let*> counts)
{
    if (st >= fn)
        return;
    char r = '0';
    int ed = fn;
    for (int i = st; i <= fn; ++i)
    {
        codes[counts[i]->lt] += r;
        if (i == fn || fn - st == 1 || (sm[i + 1] - sm[st]) > (sm[fn + 1] - sm[i + 1]))
        {
            r = '1';
            ed = i;
            break;
        }
    }
    for (int i = ed + 1; i <= fn; ++i)
        codes[counts[i]->lt] += r;
    rec(st, ed, sm, codes, counts);
    rec(ed + 1, fn, sm, codes, counts);
}

map<char, string> make_map(string text)
{
    map<char, string> codes;
    vector<let*> counts;
    string set_text = "";
    for (int i = 0; i < text.length(); ++i)
        if (count(set_text.begin(), set_text.end(), text[i]) == 0)
        {
            set_text += text[i];
            codes[text[i]] = "";
        }
    for (int i = 0; i < set_text.length(); ++i)
        counts.push_back(new let(set_text[i], count(text.begin(), text.end(), set_text[i])));
    sort(counts.begin(), counts.end(), compare_lets);
    int sm[counts.size() + 1];
    sm[0] = 0;
    for (int i = 0; i < counts.size(); ++i)
        sm[i + 1] = sm[i] + counts[i]->cnt;
    int st = 0;
    int fn = counts.size() - 1;
    char r = '0';
    int ed = 0;
    rec(st, fn, sm, codes, counts);
    return codes;
}

string code(string text, map<char, string> codes)
{
    string s = "";
    for (int i = 0; i < text.length(); ++i)
        s += codes[text[i]];
    return s;
}

string decode(string text, map<char, string> codes)
{
    string s = "";
    string buffer = "";
    for (int i = 0; i < text.length(); ++i)
    {
        buffer += text[i];
        for (auto& [lt, code] : codes)
            if (code == buffer)
            {
                s += lt;
                buffer = "";
                break;
            }
    }
    return s;
}

struct haf
{
    char lt;
    char code;
    int cnt;
    haf* left;
    haf* right;
    haf(char lt, int cnt, haf* left, haf* right, char code)
    {
        this->lt = lt;
        if (left && right)
            this->cnt = left->cnt + right->cnt;
        else
            this->cnt = cnt;
        this->left = left;
        this->right = right;
        this->code = code;
    }
    char find(string code, int ind = 0)
    {
        if (!this->left && !this->right)
            if (code.length() == ind)
                return this->lt;
            else
                return '@';
        if (ind >= code.length())
            return '@';
        if (code[ind] == '0')
            return this->left->find(code, ind + 1);
        return this->right->find(code, ind + 1);
    }
    string get_code(char lt)
    {
        if (!this->left && !this->right)
            if (this->lt == lt)
                return string(1, this->code);
            else
                return "";
        string s = this->left->get_code(lt) + this->right->get_code(lt);
        if (s != "" && this->code != '@')
            return this->code + s;
        return s;
    }
};

bool compare_hafs(const haf* pr1, const haf* pr2)
{ return pr1->cnt < pr2->cnt; }

haf* make_haf(string text)
{
    vector<haf*> cnts;
    string set_text = "";
    for (int i = 0; i < text.length(); ++i)
        if (count(set_text.begin(), set_text.end(), text[i]) == 0)
            set_text += text[i];
    for (int i = 0; i < set_text.length(); ++i)
        cnts.push_back(new haf(set_text[i], count(text.begin(), text.end(), set_text[i]), nullptr, nullptr, '@'));
    haf* ptr;
    while (cnts.size() > 1)
    {
        sort(cnts.begin(), cnts.end(), compare_hafs);
        cnts[0]->code = '0';
        cnts[1]->code = '1';
        ptr = new haf('@', 0, cnts[0], cnts[1], '@');
        cnts.push_back(ptr);
        cnts.erase(cnts.begin());
        cnts.erase(cnts.begin());
    }
    ptr = cnts[0];
    return ptr;
}

string code_h(string text, haf* codes)
{
    string s = "";
    for (int i = 0; i < text.length(); ++i)
        s += codes->get_code(text[i]);
    return s;
}

string decode_h(string text, haf* codes)
{
    string s = "";
    string buffer = "";
    char lt = '@';
    for (int i = 0; i < text.length(); ++i)
    {
        buffer += text[i];
        lt = codes->find(buffer);
        if (lt != '@')
        {
            s += lt; buffer = "";
        }
    }
    return s;
}

void ciaod_8_1()
{
    string text = "По-турецки говорили. Чяби, чяряби Чяряби, чяби-чяби. Мы набрали в рот воды.";
    map<char, string> codes = make_map(text);
    string coded_s = code(text, codes);
    string decoded_s = decode(coded_s, codes);
    cout << "\n\n\nКодирование методом Шеннона-Фано:\nИсходная строка:\nРазмер в битах: " << text.length() * 8 << endl
        << text << "\n\nЗакодированная строка:\nРазмер в битах: " << coded_s.length() << endl << coded_s << endl
        << "\nРаскодированная строка:\n" << decoded_s;

    string s = "Враженко Даниил Олегович";
    haf* codes_h = make_haf(s);
    coded_s = code_h(s, codes_h);
    decoded_s = decode_h(coded_s, codes_h);
    cout << "Кодирование методом Хаффмана:\nИсходная строка:\nРазмер в битах: " << s.length() * 8 << endl << s
        << "\n\nЗакодированная строка:\nРазмер в битах: " << coded_s.length() << endl << coded_s
        << "\n\nРаскодированная строка:\n" << decoded_s;
}

vector<vector<int>> generateRandomMatrix(int n, int m) // создание массива из случайных чисел
{
    random_device rd;
    mt19937 gen(rd());
    vector<vector<int>> arr(n, vector<int>(m, 0));
    for (int i = 0; i < n; ++i) // проход по строкам
        for (int j = 0; j < m; ++j) // проход по столбцам
            arr[i][j] = rd() % 1000; // заполнение ячейки случайным значением
    return arr;
}

void print(vector<vector<int>>& arr) // вывод матрицы на экран
{
    for (int i = 0; i < arr.size(); ++i) // проход по строкам
    {
        for (int j = 0; j < arr[0].size(); ++j) // проход по столбцам
        {
            int spaces = 1;
            if (arr[i][j] > 0)
                spaces = log10(arr[i][j]);
            spaces = 10 - spaces;
            for (int k = 0; k < spaces; k++) // вывод проьелов на экран 
                cout << ' ';
            cout << arr[i][j];
        }
        cout << '\n';
    }
}

vector<vector<int>> countVariants(int n, int m) // метод для подсчета всех возможных вариантов движения
{
    vector<vector<int>> arr(n, vector<int>(m, 0)); // создание чистого массива
    arr[0][0] = 1;
    for (int i = 1; i < n; ++i) // проход по левой границе
        arr[i][0] += arr[i - 1][0];
    for (int j = 1; j < m; ++j) // проход по верхней границе
        arr[0][j] += arr[0][j - 1];
    for (int i = 1; i < n; ++i) // проход по внутреннему содержимому
        for (int j = 1; j < m; ++j)
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] + arr[i - 1][j - 1];
    return arr; // возврат массива с числами - количеством возможных путей к данной позиции
}

int minimum(int a, int b, int c) // нахождение минимума среди трех чисел
{
    if (b < a) a = b;
    if (c < a) a = c;
    return a;
}

vector<vector<int>> minSum(vector<vector<int>>& baseArr) // нахождение минимального пути в массиве
{
    int n = baseArr.size(); // вычисление кол-ва строк
    int m = baseArr[0].size(); // вычисление кол-ва столбцов
    vector<vector<int>> arr(n, vector<int>(m, 0)); // создание пустого массива
    arr[0][0] = baseArr[0][0]; // присваивание левой верхней ячейке нового массива значение левой верхней ячейки начального массива
    for (int i = 1; i < n; ++i) // проход по левой границе
        arr[i][0] = arr[i - 1][0] + baseArr[i][0];
    for (int j = 1; j < m; ++j) // проход по верхней границе
        arr[0][j] = arr[0][j - 1] + baseArr[0][j];
    for (int i = 1; i < n; ++i) // проход по внутренней части
        for (int j = 1; j < m; ++j)
            arr[i][j] = baseArr[i][j] + minimum(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]);
    return arr;
}

void ciaod_8_2()
{
    const int n = 5, m = 2;

    cout << "Исходная матрица:\n";
    vector<vector<int>> arr = generateRandomMatrix(n, m);
    print(arr);

    cout << "\nМатрица количества вариантов:\n";
    vector<vector<int>> newArr = countVariants(n, m);
    print(newArr);

    cout << "\nМатрица минимальных значений:\n";
    vector<vector<int>> minArr = minSum(arr);
    print(minArr);
}