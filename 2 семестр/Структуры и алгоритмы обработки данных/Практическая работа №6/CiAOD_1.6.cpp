#include "struct.h"
#include "main_functions.cpp"
#include "additional_functions.cpp"
using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	Node* head = nullptr;
	Node* tail = nullptr;
	Node* returnListHead = nullptr;
	int choice;
	string main_productCode, main_saleDate; double main_price; bool main_returnMark;
	do
	{
		cout << "\nОперации\n"
			<< " 1. Вставить узел\n"
			<< " 2. Удалить узел\n"
			<< " 3. Вывести список слева направо\n"
			<< " 4. Вывести список справа налево\n"
			<< " 5. Поиск узла по коду товара\n"
			<< " 6. Сортировать список по дате продажи\n"
			<< " 7. Удалить все узлы с заданным товаром и датой продажи\n"
			<< " 8. Сформировать новый список по товарам с возвратом\n"
			<< " 0. Выйти из программы\n"
			<< "Выберите действие: ";
		cin >> choice;
		switch (choice)
		{
		case 1:
			cout << "Введите данные нового узла:\n";
			cout << "Код товара (буквенно-цифровой): ";
			cin >> main_productCode;
			cout << "Дата продажи: ";
			cin >> main_saleDate;
			cout << "Цена: ";
			cin >> main_price;
			cout << "Отметка о возврате (0 - Нет, 1 - Да): ";
			cin >> main_returnMark;
			insertNode(head, tail, main_productCode, main_saleDate, main_price, main_returnMark);
			break;
		case 2:
			cout << "Введите код товара узла для удаления: ";
			cin >> main_productCode;
			deleteNode(head, main_productCode);
			break;
		case 3:
			cout << "Список слева направо:\n";
			printListForward(head);
			break;
		case 4:
			cout << "Список справа налево:\n";
			printListBackward(tail);
			break;
		case 5:
			cout << "Введите код товара для поиска: ";
			cin >> main_productCode;
			if (Node* foundNode = searchNode(head, main_productCode))
			{
				cout << "Узел найден:\n";
				cout << foundNode->productCode << ", " << foundNode->saleDate << ", " << foundNode->price << ", " << (foundNode->returnMark ? "Да" : "Нет") << endl;
			}
			else cout << "Узел с указанным кодом товара не найден.\n";
			break;
		case 6:
			sortListBySaleDate(head);
			cout << "Список отсортирован по дате продажи.\n";
			break;
		case 7:
			cout << "Введите код товара и дату продажи для удаления соответствующих узлов:\n";
			cout << "Код товара: ";
			cin >> main_productCode;
			cout << "Дата продажи: ";
			cin >> main_saleDate;
			deleteNodesByProductAndDate(head, main_productCode, main_saleDate);
			break;
		case 8:
			returnListHead = createReturnList(head);
			cout << "Сформирован новый список из узлов с возвратом:\n";
			printListForward(returnListHead);
			while (returnListHead != nullptr)
			{
				Node* nextNode = returnListHead->next;
				delete returnListHead;
				returnListHead = nextNode;
			}
			break;
		case 0:
			cout << "Выход из программы.\n";
			break;
		default:
			cout << "Некорректный ввод. Попробуйте еще раз.\n";
		}
	} while (choice != 0);
	while (head != nullptr)
	{
		Node* nextNode = head->next;
		delete head;
		head = nextNode;
	}
	return (0);
}