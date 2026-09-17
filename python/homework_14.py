def number_sequence(start, end, even=True):
    for number in range(start, end + 1):
        if even and number % 2 == 0:
            yield number
        elif not even and number % 2 != 0:
            yield number

try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    choice = input("Какие числа вывести? (четные/нечетные): ").lower()

    if choice == "четные":
        even = True
    elif choice == "нечетные":
        even = False
    else:
        print("Ошибка: выберите 'четные' или 'нечетные'.")
        exit()

    print("Результат:")

    for number in number_sequence(start, end, even):
        print(number, end=" ")

except ValueError:
    print("Ошибка: необходимо вводить числа в правильном формате.")
