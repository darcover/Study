def count_common_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2))

list1 = [1, 2, 3, 4, 8]
list2 = [3, 4, 5, 6, 8]
print(count_common_numbers(list1, list2)) 