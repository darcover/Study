#include <iostream>
#include <cmath>
int main() {
    int A, B, C;
    std::cout << "Введите стороны A, B, C: ";
    std::cin >> A >> B >> C;
    if (A <= 0 || B <= 0 || C <= 0 || A >= 30000 || B >= 30000 || C >= 30000) {
        std::cout << "Стороны должны быть в диапазоне 0 < A,B,C < 30000" << std::endl;
        return 0;  
}

double diagonal = std::sqrt(A * A + B * B + C * C);

std::cout << "Главная диагональ параллелепипеда: " << diagonal << std::endl;

return 0;
}