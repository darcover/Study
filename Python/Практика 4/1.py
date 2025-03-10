dictionary = {'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}
key = input("Введите ключ: ")
print(f"Значение: {dictionary.get(key, 'Ключ не найден')}")