#include "struct.h"
#include <vector>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <iomanip>

bool compareBySaleDate(Node* node1, Node* node2)
{
	tm time1 = {};
	stringstream ss1(node1->saleDate);
	ss1 >> get_time(&time1, "%d.%m.%Y");
	tm time2 = {};
	stringstream ss2(node2->saleDate);
	ss2 >> get_time(&time2, "%d.%m.%Y");
	if (time1.tm_year != time2.tm_year)
		return time1.tm_year < time2.tm_year;
	if (time1.tm_mon != time2.tm_mon)
		return time1.tm_mon < time2.tm_mon;
	return time1.tm_mday < time2.tm_mday;
}

void sortListBySaleDate(Node*& head)
{
	if (head == nullptr || head->next == nullptr)
		return;
	vector<Node*> nodeVector;
	Node* current = head;
	while (current != nullptr)
	{
		nodeVector.push_back(current);
		current = current->next;
	}
	sort(nodeVector.begin(), nodeVector.end(), compareBySaleDate);
	head = nodeVector[0];
	head->prev = nullptr;
	for (size_t i = 1; i < nodeVector.size(); ++i)
	{
		nodeVector[i]->prev = nodeVector[i - 1];
		nodeVector[i - 1]->next = nodeVector[i];
	}
	nodeVector.back()->next = nullptr;
}

void deleteNodesByProductAndDate(Node*& head, string& productCode, string& saleDate)
{
	Node* current = head;
	while (current != nullptr)
	{
		Node* nextNode = current->next;
		if (current->productCode == productCode && current->saleDate == saleDate)
		{
			if (current->prev != nullptr)
				current->prev->next = current->next;
			if (current->next != nullptr)
				current->next->prev = current->prev;
			if (current == head)
				head = current->next;
			delete current;
		}
		current = nextNode;
	}
}

Node* createReturnList(Node* head)
{
	Node* returnHead = nullptr;
	Node* returnTail = nullptr;
	Node* current = head;
	while (current != nullptr)
	{
		if (current->returnMark)
		{
			Node* newNode = new Node;
			newNode->productCode = current->productCode;
			newNode->saleDate = current->saleDate;
			newNode->price = current->price;
			newNode->returnMark = current->returnMark;
			newNode->prev = returnTail;
			newNode->next = nullptr;
			if (returnHead == nullptr)
				returnHead = newNode;
			else
				returnTail->next = newNode;
			returnTail = newNode;
		}
		current = current->next;
	}
	return returnHead;
}