#include <iostream>
using namespace std;

//Алгоритм 1----------------------------
//int delFirstMetod(int* x, int n, int key);
//
//int main() {
//	int n; cin >> n;
//	int* x = new int[n];
//	srand(time(0));
//	for (int i = 0; i < n; i++)
//		*(x + i) = rand() % 11;
//	int key; cin >> key; cout << endl << endl;
//	cout << "n = " << n << endl << "x = [ ";
//	for (int i = 0; i < n; i++)
//		cout << *(x + i) << " ";
//	cout << "]" << endl << "key = " << key << endl << endl;
//	cout << "sum = " << delFirstMetod(x, n, key);
//	delete[] x;
//}
//
//int delFirstMetod(int* x, int n, int key) {
//	int i = 0;
//	int sum = 1;
//	while (i < n) {
//		sum++;
//		if (x[i] == key) {
//			//удаление
//			for (int j = i; j < n - 1; j++) {
//				sum++;
//				x[j] = x[j + 1];
//				sum++;
//			}
//			sum++;
//			n = n - 1;
//			sum++;
//		}
//		else {
//			i = i + 1;
//			sum++;
//		}
//		sum++;
//	}
//	sum++;
//	cout << "x = [ ";
//	for (int i = 0; i < n; i++)
//		cout << *(x + i) << " ";
//	cout << "]" << endl;
//	return sum;
//}

//Алгоритм 2----------------------------
//int delOtherMetod(int* x, int n, int key);
//
//int main() {
//	int n; cin >> n;
//	int* x = new int[n];
//	srand(time(0));
//	for (int i = 0; i < n; i++)
//		*(x + i) = rand() % 11;
//		//*(x + i) = 5;
//	int key; cin >> key; cout << endl << endl;
//	cout << "n = " << n << endl << "x = [ ";
//	for (int i = 0; i < n; i++)
//		cout << *(x + i) << " ";
//	cout << "]" << endl << "key = " << key << endl << endl;
//	cout << "sum = " << delOtherMetod(x, n, key);
//	delete[] x;
//}
//
//int delOtherMetod(int* x, int n, int key) {
//	int j = 0;
//	int sum = 1;
//	for (int i = 0; i < n; i++) {
//		sum++;
//		x[j] = x[i];
//		sum++;
//		if (x[i] != key) {
//			j++;
//			sum++;
//		}
//		sum++;
//	}
//	sum++;
//	n = j;
//	sum++;
//	cout << "x = [ ";
//	for (int i = 0; i < n; i++)
//		cout << *(x + i) << " ";
//	cout << "]" << endl;
//	return sum;
//}


//Самостоятельная работа----------------------------
// Найти минимальное четное число в части матрицы – между главной и
// побочной диагоналями (диагонали образуют вертикальные песочные часы).

int main()
{
	cout << "N = "; int N; cin >> N;
	srand(time(0));
	/*int* mat = new int[N * N];
	long x = N * N * 5;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			*(mat + i * N + j) = x;
			x -= 2;
		}
	}*/
	int* matrix = new int[N * N];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			*(matrix + i * N + j) = rand() % 100 + 1;
			//*(matrix + i * N+ j) = *(mat + i * N + j);
			cout << *(matrix + i * N + j);
			if (j < N - 1)
				cout << " ";
		}
		cout << endl;
	}
	//delete[] mat;
	int sum = 0;
	long min_matrix = N * N * 5 + 1;
	sum++;
	for (int i = 0; i < N; i++) {
		sum++;
		for (int j = 0; j < N; j++) {
			sum++;
			if ((i < j && i < (N - 1 - j)) || (i > j && i > (N - 1 - j))) {
				if ((*(matrix + i * N + j) < min_matrix) && *(matrix + i * N + j) % 2 == 0) {
					min_matrix = *(matrix + i * N + j);
					sum++;
				}
				sum++;
			}
			sum++;
		}
		sum++;
	}
	sum++;
	delete[] matrix;
	if (min_matrix != 100 + 1)
		cout << "min_matrix = " << min_matrix;
	else
		cout << "The required element was not found!";
	sum++;
	cout << endl << "sum = " << sum;
}