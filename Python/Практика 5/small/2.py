with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]
numbers.sort()
with open('sorted_numbers.txt', 'w') as f:
    for num in numbers:
        f.write(str(num) + '\n')