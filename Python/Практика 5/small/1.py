with open('input.txt', 'r') as f:
    numbers = list(map(int, f.readline().split()))
product = 1
for num in numbers:
    product *= num
with open('output.txt', 'w') as f:
    f.write(str(product))
    