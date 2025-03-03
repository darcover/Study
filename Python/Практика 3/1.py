def swap_max_min(numbers):
    
    min_idx = numbers.index(min(numbers))
    max_idx = numbers.index(max(numbers))
    
    result = numbers.copy()
    result[min_idx], result[max_idx] = result[max_idx], result[min_idx]
    return result


numbers = [1, 5, 3, 2, 4]
print(swap_max_min(numbers)) 