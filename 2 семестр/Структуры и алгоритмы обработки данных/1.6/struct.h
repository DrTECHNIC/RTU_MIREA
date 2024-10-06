#ifndef _STRUCT_H
#define _STRUCT_H
#include <iostream>
#include <string>
using namespace std;

struct Node
{
	string productCode;
	string saleDate;
	double price;
	bool returnMark;
	Node* prev = nullptr;
	Node* next = nullptr;
};

Node* createList();
void insertNode(Node*& head, const string& productCode, const string& saleDate, double price, bool returnMark);
void deleteNode(Node*& head, const string& productCode);
void printListForward(const Node* head);
void printListBackward(const Node* tail);
Node* searchNode(const Node* head, const string& productCode);

#endif