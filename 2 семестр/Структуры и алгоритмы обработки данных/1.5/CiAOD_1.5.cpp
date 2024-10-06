#include <iostream>
using namespace std;

struct list;
struct Node {
    int val;
    Node* next;
    list* list_ptr;
    Node(int _val) : val(_val), next(nullptr) {}
};
struct list {
    Node* first;
    Node* last;
    Node* array[10];
    list() : first(nullptr), last(nullptr) {}
    bool is_empty()
    {
        return first == nullptr;
    }
    void push_back(int _val) {
        Node* p = new Node(_val);
        if (is_empty()) 
        {
            first = p;
            last = p;
            return;
        }
        last->next = p;
        last = p;
    }
    void print() 
    {
        if (is_empty())
            return;
        Node* p = first;
        cout << "Список L: ";
        while (p)
        {
            cout << p->val << " ";
            p = p->next;
        }
        cout << endl;
    }
    Node* find(int _val) 
    {
        Node* p = first;
        while (p && p->val != _val)
            p = p->next;
        return (p && p->val == _val) ? p : nullptr;
    }
    void remove_first() 
    {
        if (is_empty())
            return;
        Node* p = first;
        first = p->next;
        delete p;
    }
    void remove_last() 
    {
        if (is_empty())
            return;
        if (first == last) 
        {
            remove_first();
            return;
        }
        Node* p = first;
        while (p->next != last)
            p = p->next;
        p->next = nullptr;
        delete last;
        last = p;
    }
    void remove(int _val) 
    {
        if (is_empty())
            return;
        if (first->val == _val)
        {
            remove_first();
            return;
        }
        else if (last->val == _val) 
        {
            remove_last();
            return;
        }
        Node* slow = first;
        Node* fast = first->next;
        while (fast && fast->val != _val)
        {
            fast = fast->next;
            slow = slow->next;
        }
        if (!fast) 
        {
            cout << "Этого числа не существует в списке" << endl;
            return;
        }
        slow->next = fast->next;
        delete fast;
    }
    void create1()
    {
        for (int i = 0; i < 10; ++i)
            array[i] = nullptr;
        Node* current = first;
        while (current != nullptr)
        {
            int digit = current->val / 10;
            if (array[digit] == nullptr)
            {
                array[digit] = new Node(current->val);
                array[digit]->list_ptr = this;
                first = array[digit];
                last = array[digit];
            }
            else
            {
                last->next = new Node(current->val);
                last = last->next;
                last->list_ptr = this;
            }
            current = current->next;
        }
        cout << "Список указателей A:\n";
        for (int i = 0; i < 10; ++i)
        {
            Node* temp = array[i];
            cout << "Список " << i << ": ";
            while (temp != nullptr)
            {
                cout << temp->val << ' ';
                temp = temp->next;
            }
            cout << endl;
        }
    }
    void del() 
    {
        Node* current = first;
        while (current != nullptr)
        {
            Node* next = current->next;
            delete current;
            current = next;
        }
        first = nullptr;
        last = nullptr;
    }
    void create2()
    {
        del();
        for (int i = 0; i < 10; i++)
            while (array[i] != nullptr)
            {
                push_back(array[i]->val);
                array[i] = array[i]->next;
            }
    }
};
list create(int n) 
{
    list b;
    int k;
    for (int i = 0; i < n; i++)
    {
        cout << "Введите число: ";
        cin >> k;
        b.push_back(k);
    }
    return b;
}

int main()
{
    setlocale(LC_ALL, "Russian");
    list L; bool flag = true;
    while (flag == true)
    {
        cout << "\nОперации:\n"
            << "     1. Добавить число в конец списка\n"
            << "     2. Удалить число по значению\n"
            << "     3. Создать свой собственный список\n"
            << "     4. Использовать готовый список\n"
            << "     5. Вывести на экран список\n"
            << "     6. Создать список A из 10 указателей на элемент списка\n"
            << "     7. Удалить список\n"
            << "     8. Создать список L и включить в него списки массива A\n"
            << "     Любое другое число - выход из программы\n"
            << "Ввод: ";
        int action;
        cin >> action;
        switch (action)
        {
        case (1):
            cout << "Введите число: ";
            int element;
            cin >> element;
            L.push_back(element);
            break;
        case(2):
            cout << "Введите число: ";
            cin >> element;
            L.remove(element);
            create;
            break;
        case(3):
            cout << "Введите размер списка: ";
            cin >> element;
            L = create(element);
            break;
        case(4):
            L = list();
            L.push_back(12); L.push_back(53); L.push_back(34); L.push_back(83); L.push_back(62); L.push_back(71); L.push_back(75); L.push_back(6); L.push_back(9);
            break;
        case(5):
            L.print();
            break;
        case(6):
            L.create1();
            break;
        case(7):
            L.del();
            break;
        case(8):
            L.create2();
            break;
        default:
            flag = false;
        }
    }
}