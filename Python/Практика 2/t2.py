from collections import Counter

def top_three_chars(s):
    s = s.replace(" ", "")  
    counter = Counter(s)
    most_common = counter.most_common(3)
    
    for char, count in most_common:
        print(f"{char}: {count}")

s = input("Введите строку: ")
top_three_chars(s)
