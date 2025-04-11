#include "struct.h"

Node* createList()
{ return nullptr; }

void insertNode(Node*& head, Node*& tail, string& productCode, string& saleDate, double price, bool returnMark)
{
	Node* newNode = new Node;
	newNode->productCode = productCode;
	newNode->saleDate = saleDate;
	newNode->price = price;
	newNode->returnMark = returnMark;
	newNode->prev = tail;
	newNode->next = nullptr;
	if (tail != nullptr)
		tail->next = newNode;
	tail = newNode;
	if (head == nullptr)
		head = newNode;
}

void deleteNode(Node*& head, string& productCode)
{
	Node* current = head;
	while (current != nullptr)
	{
		if (current->productCode == productCode)
		{
			if (current->prev != nullptr)
				current->prev->next = current->next;
			if (current->next != nullptr)
				current->next->prev = current->prev;
			if (current == head)
				head = current->next;
			delete current;
			return;
		}
		current = current->next;
	}
}

void printListForward(Node* head)
{
	Node* current = head;
	while (current != nullptr)
	{
		cout << current->productCode << ", " << current->saleDate << ", " << current->price << ", " << (current->returnMark ? "Да" : "Нет") << endl;
		current = current->next;
	}
}

void printListBackward(Node* tail)
{
	Node* current = tail;
	while (current != nullptr)
	{
		cout << current->productCode << ", " << current->saleDate << ", " << current->price << ", " << (current->returnMark ? "Да" : "Нет") << endl;
		current = current->prev;
	}
}

Node* searchNode(Node* head, string& productCode)
{
	Node* current = head;
	while (current != nullptr)
	{
		if (current->productCode == productCode)
			return const_cast<Node*>(current);
		current = current->next;
	}
	return nullptr;
}