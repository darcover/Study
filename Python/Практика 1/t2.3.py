def inverted_pyramid(n):
    width = len("".join(str(i) for i in range(1, n + 1)) + "".join(str(i) for i in range(n, 0, -1)))  
    for i in range(n, 0, -1):
        row = "".join(str(j) for j in range(i, 0, -1)) + "".join(str(j) for j in range(2, i + 1))
        print(row.center(width))

n = int(input("Введите число n: "))
inverted_pyramid(n)