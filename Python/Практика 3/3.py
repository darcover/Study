def count_string_repetitions(strings):
    count_dict = {}
    for string in strings:
        count_dict[string] = count_dict.get(string, 0) + 1
    
    return list(count_dict.values())

test1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
print(*count_string_repetitions(test1)) 