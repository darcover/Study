dictionary = {'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}
value = input("Введите значение: ")
key = next((k for k, v in dictionary.items() if v == value), "Значение не найдено")
print(f"Ключ: {key}")