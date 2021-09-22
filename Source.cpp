#include <iostream>
#include <vector>
/*   ������ � ������� 
	 * n - ����� �������
	 * b - ��� ������� (����������: [0;n-2])
	 * c - ������� ��������� (����������: [0;n-1])
	 * a - ��� ������� (����������: [1;n-1])
	 * d - �������
	 * x - �������
*/
void solveTriagonalSlae(int n, std::vector<double>& a, std::vector<double>& c, std::vector<double>& b, std::vector<double>& d, std::vector<double>& x) {

	double m;
	for (int i = 1; i < n; i++) {
		m = a[i] / c[i - 1];
		c[i] = c[i] - m * b[i - 1];
		d[i] = d[i] - m * d[i - 1];
	}

	x[n - 1] = d[n - 1] / c[n - 1];

	for (int i = n - 2; i >= 0; i--) {
		x[i] = (d[i] - b[i] * x[i + 1]) / c[i];
	}
}


int main() {

	setlocale(LC_ALL, "Russian");

	std::cout << "���������� ����� �������: " << std::endl;
	int n;
	std::cin >> n;
	
	double num;

	std::cout << "������� ���������: " << std::endl;
	std::vector<double> a;
	for (int i = 0; i < n-1; i++) {
		std::cin >> num;
		a.push_back(num);
	}
	
	std::cout << "������� ���������: " << std::endl;
	std::vector<double> b;
	for (int i = 0; i < n; i++) {
		std::cin >> num;
		b.push_back(num);
	}
	b[n - 1] = 0;
	std::cout << "������ ���������: " << std::endl;
	std::vector<double> c;
	for (int i = 1; i < n; i++) {
		std::cin >> num;
		c.push_back(num);
	}
	c[0] = 0;
	std::cout << "������� " << std::endl;
	std::vector<double> d;
	for (int i = 0; i < n; i++) {
		std::cin >> num;
		d.push_back(num);
	}
	
	std::vector<double>x;
	
	solveTriagonalSlae(n, c, b, a, d, x);
	
	std::cout << "����� " << std::endl;
	for (int i = 0; i < n; i++) {
		std::cout << x[i] << " ";
	}

	return 0;
}