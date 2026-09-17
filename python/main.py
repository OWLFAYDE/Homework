#1
try:
    print("Калькулятор целых чисел: ")
    num1=int(input("введите 1 число: "))
    num2=int(input("введите 2 число: "))
    num3=int(input("введите 3 число: "))
    print(f"{num1}+{num2}+{num3}={num1+num2+num3} ")
    print(f"{num1}*{num2}*{num3}={num1*num2*num3} ")
except ValueError:           #Если пользователь введет не число
    print("Ошибка: пожалуйста вводите только числа! ")

#2
print("Счетчик твоих расходов: ")
num1=float(input("введите зарплату за месяц: "))
num2=float(input("введите месячный платеж по кредиту: "))
num3=float(input("введите платеж по коммунальным услугам: "))
print(f"{num1}-{num2}-{num3}={num1-num2-num3} ")
print(f"ваш остаток:={num1-num2-num3}")

#3
print("Вычеслим площадь ромба по диагоналям: ")
d1=float(input("введите длину 1 диагонали ромба: ")) #d1/d2 по геометерическому смыслу от diagonal
d2=float(input("введите длину 2 диагонали ромба: "))
print(f"{d1}*{d2}/2={d1*d2/2} ")
print(f"Ответ S ромба:={d1*d2/2} ")

#4
print("To be\nor not\nto be") #Выводит текст <To be or not tobe> на разные строки.

#5
print("«Life is what happens\n\twhen\n\t\tyou're busy making other plans»\n\t\t\t\t\t\t\t\t\tJohn Lennon. ")
