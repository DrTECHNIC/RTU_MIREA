#include <iostream>
#include <string>
using namespace std;

int deldot(double number)
{
    string str = to_string(number);
    size_t dot = str.find(',');
    if (dot != string::npos)
    {
        string str1 = str.substr(0, dot);
        string str2 = str.substr(dot + 1);
        while (str2[str2.size() - 1] == '0')
            str2.erase(str2.size() - 1, 1);
        str = str1 + str2;
    }
    return stoi(str);
}
int func_1(int number)
{
    int sum = 0;
    while (number > 0)
    {
        sum += number % 10;
        number /= 10;
    }
    if (sum < 10)
        return sum;
    return func_1(sum);
}

struct Node {
    int data;
    Node* prev;
    Node* next;
    Node(int val) : data(val), prev(nullptr), next(nullptr) {}
};
class DLL {
private:
    Node* head;
    Node* tail;
    int size;
    int count(Node* node)
    {
        if (!node) return 0;
        return (node->data % 2 == 0 ? 1 : 0) + count(node->next);
    }
public:
    DLL() : head(nullptr), tail(nullptr), size(0) {}
    void add(int val)
    {
        Node* newNode = new Node(val);
        if (!head) head = tail = newNode;
        else
        {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
        size++;
    }
    int count()
    { return count(head); }
    void print()
    {
        Node* current = head;
        while (current)
        {
            cout << current->data << ' ';
            current = current->next;
        }
        cout << endl;
    }
};

int main()
{
    setlocale(LC_ALL, "Russian");
    cout << "Введите номер задания (1, 2): "; int choice; cin >> choice;
    if (choice == 1)
    {
        cout << "Введите число: "; double n; cin >> n;
        int number = deldot(n);
        int result = func_1(number);
        cout << "Цифровой корень: " << result;
    }
    else if (choice == 2)
    {
        DLL func_2;
        func_2.add(1); func_2.add(2); func_2.add(4); func_2.add(5); func_2.add(6); func_2.add(8);
        cout << "Двунаправленный список: "; func_2.print();
        int result = func_2.count();
        cout << "Кол-во чётных элементов: " << result;
    }
    return 0;
}