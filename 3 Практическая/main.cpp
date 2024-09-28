#include <iostream>

using namespace std;

void setBit(int x, int i) {
  if (i < 0 || i >= 32) {
    cout << "Некорректный номер бита" << endl;
    return; 
  }

  int mask = 1 << i;
  x |= mask; // Можно использовать комбинированное присваивание

  cout << "Результат: " << x << endl; // Выводим результат в функции
}

int main() {
  int x, i;

  cout << "Введите число x: ";
  cin >> x;

  cout << "Введите номер бита i (от 0 до 31): ";
  cin >> i;

  setBit(x, i); // Вызываем функцию без присваивания результата

  return 0;
}