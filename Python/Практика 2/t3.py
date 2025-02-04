from num2words import num2words

def number_to_words(n):
        print(num2words(n, lang="ru"))

n = int(input("Введите число от 1 до 1000: "))
number_to_words(n)