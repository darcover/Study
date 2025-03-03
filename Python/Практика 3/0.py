def get_greater_than_previous(numbers):
    result = []
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            result.append(numbers[i])
    return result

numbers = [1, 2, 0, 3, 2, 4]
print(get_greater_than_previous(numbers))  