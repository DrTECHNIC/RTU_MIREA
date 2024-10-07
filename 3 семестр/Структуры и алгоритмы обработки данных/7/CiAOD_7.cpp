#include <Windows.h>
#include <iostream>
#include <queue>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

void ciaod_7_1();
void ciaod_7_2();

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    ciaod_7_1(); // ciaod_7_1() / ciaod_7_2()
    return 0;
}

struct avl
{

private:

    int count() // метод для подсчета количества всех узлов
    {
        int count = 1;
        if (this->left) 
            count += this->left->count();
        if (this->right)
            count += this->right->count();
        return count;
    }

    double sum() // метод для подсчета суммы значений всех узлов
    {
        int sum = this->value;
        if (this->left)
            sum += this->left->sum();
        if (this->right)
            sum += this->right->sum();
        return sum;
    }

public:

    double value;
    avl* left;
    avl* right;
    int height;

    avl(double value) // конструктор дерева
    {
        this->value = value;
        this->left = nullptr;
        this->right = nullptr;
        this->height = 1;
    }

    void postOrder() // обратный обход
    {
        if (this->left)
            this->left->postOrder();
        if (this->right)
            this->right->postOrder();
        cout << this->value << ' ';
    }

    void inOrder() // симметричный обход
    {
        if (this->left)
            this->left->inOrder();
        cout << this->value << ' ';
        if (this->right)
            this->right->inOrder();
    }

    double leavesSum() // метод для подсчета суммы значений всех листьев
    {
        if (!this->left && !this->right)
            return this->value;
        double sum = 0;
        if (this->left)
            sum += this->left->leavesSum();
        if (this->right)
            sum += this->right->leavesSum();
        return sum;
    }

    double avg() // метод для нахождения среднего арифметического всех узлов
    { return this->sum() / this->count(); }

    int findLength(double value) // метод для нахождения длины дерева
    {
        if (this->value == value)
            return 0;
        int mn = 1000;
        int x;
        if (this->left)
        {
            x = this->left->findLength(value);
            mn = x < mn ? x : mn;
        }
        if (this->right)
        {
            x = this->right->findLength(value);
            mn = x < mn ? x : mn;
        }
        return mn + 1;
    }

    void showTree(avl* root) // метод для вывода дерева на экран
    {
        cout << string((root->findLength(this->value)) * 4, ' ') << this->value << '\n';
        if (this->left)
            this->left->showTree(root);
        if (this->right)
            this->right->showTree(root);
    }
};

int height(avl* tree) // функция для нахождения высоты дерева
{ return tree ? tree->height : 0; }

int bFactor(avl* tree) // Б-фактор
{ return height(tree->right) - height(tree->left); }

void fixHeight(avl* tree) // метод для исправления глубины дерева
{
    int height_left = height(tree->left);
    int height_right = height(tree->right);
    tree->height = (height_left > height_right ? height_left : height_right) + 1;
}

avl* rotateRight(avl* old_tree) // метод для поворота дерева направо
{
    avl* new_tree = old_tree->left;
    old_tree->left = new_tree->right;
    new_tree->right = old_tree;
    fixHeight(old_tree);
    fixHeight(new_tree);
    return new_tree;
}

avl* rotateLeft(avl* old_tree) // метод для поворота дерева налево
{
    avl* new_tree = old_tree->right;
    old_tree->right = new_tree->left;
    new_tree->left = old_tree;
    fixHeight(old_tree);
    fixHeight(new_tree);
    return new_tree;
}

avl* balance(avl* tree) // метод для балансировки дерева
{
    fixHeight(tree);
    if (bFactor(tree) == 2)
    {
        if (bFactor(tree->right) < 0)
            tree->right = rotateRight(tree->right);
        return rotateLeft(tree);
    }
    if (bFactor(tree) == -2)
    {
        if (bFactor(tree->left) > 0)
            tree->left = rotateLeft(tree->left);
        return rotateRight(tree);
    }
    return tree; // балансировка не нужна
}

avl* insert(avl* tree, double new_data) // метод для ввода новых данных в дерево
{
    if (!tree)
        return new avl(new_data);
    if (new_data < tree->value)
        tree->left = insert(tree->left, new_data);
    else
        tree->right = insert(tree->right, new_data);
    return balance(tree);
}

void ciaod_7_1()
{
    avl* tree = nullptr;
    while (true)
    {
        cout << "\nЧто вы хотите сделать?\n1 - Вывод содержимого\n2 - Добавление записи\n3 - Обратный обход\n"
            << "4 - Симметричный обход\n5 - Сумма значений листьев\n6 - Среднее арифметическое всех узлов\n"
            << "0 - Выход\nНомер действия: ";
        int choise; cin >> choise; cout << endl;
        if (choise == 2)
        {
            cout << "Введите данные новой записи: ";
            double new_data; cin >> new_data;
            tree = insert(tree, new_data);
            continue;
        }
        if (!tree)
        {
            cout << "Дерево пока что пустое, нечего выводить\n";
            continue;
        }
        if (choise == 1)
        {
            cout << "AVL дерево:\n";
            tree->showTree(tree);
        }
        else if (choise == 3)
            tree->postOrder();
        else if (choise == 4)
            tree->inOrder();
        else if (choise == 5)
            cout << "Сумма значений листьев: " << tree->leavesSum();
        else if (choise == 6)
            cout << "Среднее арифметическое узлов: " << tree->avg();
        else if (choise == 0)
        {
            delete tree;
            return;
        }
        else
            cout << "Неизвестная команда.";
    }
}

vector<vector<int>> enterGraph(int n) // метод для ввода данных в граф
{
    vector<vector<int>> graph(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i) // перебор строк графа
    {
        cout << "Введите веса дуг, исходящих из вершины " << i << ": ";
        for (int j = 0; j < n; ++j) // перебор столбцов графа
        {
            int num;
            cin >> num;
            graph[i][j] = num;
        }
    }
    return graph;
}

vector<vector<int>> readGraph() // метод для чтения данных из графа
{
    ifstream file("text.txt");
    int num, n;
    file >> n;
    vector<vector<int>> graph(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i) // проход по строкам графа
        for (int j = 0; j < n; ++j) // проход по столбцам графа
        {
            file >> num;
            graph[i][j] = num;
        }
    file.close();
    return graph;
}

void buildGraph(vector<vector<int>>& graph) // создание нового графа
{
    int n = graph.size();
    int inf = 999;
    for (int i = 0; i < n; ++i) // проход по строкам графа
        for (int j = 0; j < n; ++j) // проход по столбцам графа
            if (graph[i][j] == 0 && i != j)
                graph[i][j] = inf;
    for (int k = 0; k < n; ++k) // проход по индексу k
        for (int i = 0; i < n; ++i) // проход по индексу i
            for (int j = 0; j < n; ++j) // проход по индексу j
                if (graph[i][k] + graph[k][j] < graph[i][j])
                    graph[i][j] = graph[i][k] + graph[k][j];
}

void showGraph(vector<vector<int>>& graph) // метод для вывода графа на экран
{
    int n = graph.size();
    cout << "  \\ ";
    int offset = 0;
    for (int i = 0; i < n; ++i)
    {
        offset = (int)log10(i);
        offset = offset < 0 ? 0 : offset;
        cout << string(3 - offset, ' ') << i;
    }
    cout << "\n   \\" << string(n * 4 + 1, '-') << endl;
    for (int i = 0; i < n; ++i) // проход по строкам графа
    {
        offset = (int)log10(i);
        offset = offset < 0 ? 0 : offset;
        cout << string(2 - offset, ' ') << i << "|";
        for (int j = 0; j < n; ++j) // проход по столбцам графа
        {
            int num = graph[i][j];
            if (num != 999)
            {
                offset = (int)log10(num);
                offset = offset < 0 ? 0 : offset;
                cout << string(3 - offset, ' ') << num;
            }
            else
                cout << "   -";
        }
        cout << endl;
    }
}

void ciaod_7_2()
{
    vector<vector<int>> graph;
    int n, i, j, s;
    while (true)
    {
        int choise;
        cout << "\nЧто вы хотите сделать?\n1 - Ввод графа с клавиатуры"
            << "\n2 - Ввод графа из файла\n0 - Выход\nНомер действия: ";
        cin >> choise;
        if (choise == 1)
        {
            cout << "Введите количество вершин графа: ";
            cin >> n;
            graph = enterGraph(n);
            cout << "\nГраф считан:\n\n";
        }
        else if (choise == 2)
        {
            cout << "Граф считан из файла:\n\n";
            graph = readGraph();
        }
        else if (choise == 0)
            return;
        else
        {
            cout << "Неизвестная команда.";
            cout << endl;
            continue;
        }
        showGraph(graph);
        cout << "\nВведите номера начального и конечного узлов: ";
        cin >> i >> j;
        cout << "Матрица кратчайших путей:\n\n";
        buildGraph(graph);
        showGraph(graph);
        s = graph[i][j];
        cout << endl;
        if (s == 999)
            cout << "Между этими узлами нет соединения." << endl;
        else
            cout << "Расстояние между " << i << " и " << j << ": " << s;
        cout << endl;
    }
}