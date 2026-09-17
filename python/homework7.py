num1 = int(input("Введите число :"))
num2 = int(input("Введите число :"))
num3 = int(input("Введите число :"))
num4 = int(input("Введите число :"))
if num1 == num2 and num1 == num3 and num1 == num4:
    print("Числа равны")
else:
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    if num4 > max_num:
        max_num = num4
    print("Наибольшее число", max_num)

n = int(input("Введите сторону квадрата: "))
for p in range(n):
    for j in range(n):
        if j >= p and j <= n - 1 - p:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
