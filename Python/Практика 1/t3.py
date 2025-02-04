def PrintPasTriangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0]+row, row+[0])]
        
n = int(input("Введите число n: "))

PrintPasTriangle(n)