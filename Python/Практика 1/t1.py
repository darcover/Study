
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

if num1 <= num2 and num1 <= num3:
    min_num = num1
elif num2 <= num1 and num2 <= num3:
    min_num = num2
else:
    min_num = num3

print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")