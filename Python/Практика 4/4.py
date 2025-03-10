from collections import Counter

string = input("Введите строку чисел: ")
result = dict(Counter(string).most_common(3))
print(f"Топ-3: { {int(k): v for k, v in result.items()} }")