// Учет выдачи книг пользователям библиотеки. Карточка пользователя 
// библиотеки содержит сведения, о выданной книге: Номер читательского 
// билета, Инвентарный номер, Автор, Название, Дата выдачи, Дата возврата
#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <vector>
#include <algorithm>
using namespace std;

void printFile(const string& filename)
{
	ifstream file(filename);
	string line;
	while (getline(file, line))
		cout << line << endl;
	file.close();
}

void Sort(int arr[], int n)
{
	int i, j, min_idx;
	for (i = 0; i < n - 1; i++) {
		min_idx = i;
		for (j = i + 1; j < n; j++) {
			if (arr[j] < arr[min_idx])
				min_idx = j;
		}
		if (min_idx != i)
			swap(arr[min_idx], arr[i]);
	}
}
void firstMergeSort(string A, string B, string C, int len)
{
	int n = 1;
	while (n < len)
	{
		ifstream fAi; ofstream fBo, fCo; //Фаза разделения
		fAi.open(A); fBo.open(B); fCo.open(C);
		int k = 0;
		string ch;
		while (!fAi.eof())
		{
			ch = "";
			fAi >> ch;
			if (k % 2 == 0)
				fBo << ch << ' ';
			else
				fCo << ch << ' ';
			k++;
		}
		fAi.close(); fBo.close(); fCo.close();
		ofstream fAo; ifstream fBi, fCi; //Фаза слияния
		fAo.open(A); fBi.open(B); fCi.open(C);
		string b, c; k = 0; int kol = 0;
		int* mas = new int[len * 2];
		while (!fBi.eof())
		{
			b = ""; fBi >> b;
			if (b != "")
			{
				mas[k] = stoi(b);
				k++;
			}
			kol++;
			c = ""; fCi >> c;
			if (c != "")
			{
				mas[k] = stoi(c);
				k++;
			}
			kol++;
			if (kol % (n * 2) == 0)
			{
				Sort(mas, k);
				for (int i = 0; i < k; i++)
					fAo << mas[i] << ' ';
				k = 0;

			}
		}
		fAo.close(); fBi.close(); fCi.close();
		n *= 2;
	}
}
struct Person
{
	int readerCardNumber;
	string other;
};
void Sort(vector <Person>& people) {
	sort(people.begin(), people.end(), [](const Person& a, const Person& b) { return a.readerCardNumber < b.readerCardNumber; });
}
void SplitAndSort(const string& A, const string& B, const string& C) 
{
	ifstream Fin(A); ofstream Fout1(B), Fout2(C);
	string line; int linereaderCardNumber = 0;
	while (getline(Fin, line))
	{
		if (linereaderCardNumber % 2 == 0)
			Fout1 << line << endl;
		else
			Fout2 << line << endl;
		++linereaderCardNumber;
	}
	Fin.close(); Fout1.close(); Fout2.close();
}
void MergeFiles(const string& A, const string& B, const string& C) 
{
	ofstream Fout(A); ifstream Fin1(B), Fin2(C);
	vector <Person> people; Person person; string line;
	while (getline(Fin1, line))
	{
		size_t pos = line.find(',');
		person.readerCardNumber = stoi(line.substr(0, pos));
		person.other = line.substr(pos + 1);
		people.push_back(person);
	}
	while (getline(Fin2, line)) 
	{
		size_t pos = line.find(',');
		person.readerCardNumber = stoi(line.substr(0, pos));
		person.other = line.substr(pos + 1);
		people.push_back(person);
	}
	Sort(people);
	for (const auto& p : people)
		Fout << p.readerCardNumber << ',' << p.other << endl;
	Fout.close(); Fin1.close(); Fin2.close();
}
void StraightMerge(const string& A, const string& B, const string& C)
{
	if (A == "A1.txt")
		firstMergeSort(A, B, C, 15);
	else
	{
		SplitAndSort(A, B, C);
		MergeFiles(A, B, C);
	}
}
void naturalSplitAndSort(const string& A)
{
	string B = "B.txt", C = "C.txt";
	ifstream Fin(A); ofstream Fout1(B), Fout2(C);
	string line; int linereaderCardNumber = 0;
	while (getline(Fin, line))
	{
		if (linereaderCardNumber % 2 == 0)
			Fout1 << line << endl;
		else
			Fout2 << line << endl;
		++linereaderCardNumber;
	}
	Fin.close(); Fout1.close(); Fout2.close();
}
void naturalMergeSort(const string& A)
{
	string B = "B.txt", C = "C.txt";
	ofstream Fout(A); ifstream Fin1(B), Fin2(C);
	vector <Person> people; Person person; string line;
	while (getline(Fin1, line))
	{
		size_t pos = line.find(',');
		person.readerCardNumber = stoi(line.substr(0, pos));
		person.other = line.substr(pos + 1);
		people.push_back(person);
	}
	while (getline(Fin2, line))
	{
		size_t pos = line.find(',');
		person.readerCardNumber = stoi(line.substr(0, pos));
		person.other = line.substr(pos + 1);
		people.push_back(person);
	}
	Sort(people);
	for (const auto& p : people)
		Fout << p.readerCardNumber << ',' << p.other << endl;
	Fout.close(); Fin1.close(); Fin2.close();
}
void NaturalMerge(const string& A)
{
	naturalSplitAndSort(A);
	naturalMergeSort(A);
}



int main()
{
	setlocale(LC_ALL, "Russian");
	string A = "A2.txt", B = "B.txt", C = "C.txt";
	cout << "\nUnsorted A file:\n"; printFile(A);
	int start_time = clock();
	StraightMerge(A, B, C);
	//NaturalMerge(A);
	int end_time = clock();
	cout << "\nSorted A file:\n"; printFile(A);
	cout << "\n\n\nWork time = " << end_time - start_time;
	return 0;
}