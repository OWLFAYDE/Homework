#1
age = int(input("Введите свой возраст: "))
if age>= 0 and age < 13:
    print("вы ребенок")
elif age>= 13 and age < 18:
    print("вы подросток")
elif age>= 18 and age<= 60:
    print("вы взрослый")
elif age > 60:
    print("вы пенсионер")
else:
    print("введен не коректный возраст")
#2
num = int(input("введите число от 0 до 9: "))
if num < 0 or num > 9:
    print("ошибка введено некоректное число")
elif num == 1:
    print("!")
elif num == 2:
    print("@")
elif num == 3:
    print("#")
elif num == 4:
    print("$")
elif num == 5:
    print("%")
elif num == 6:
    print("^")
elif num == 7:
    print("&")
elif num == 8:
    print("*")
elif num == 9:
    print("(")
elif num == 0:
    print(")")

#3
num = input("введите число: ")
d1 = num[0]
d2 = num[1]
d3 = num[2]
if d1==d2 or d1==d3 or d2==d3:
    print("в числе есть одинаковые цифры")
else:
    print("все числа разные")

#4
year = int(input("введите год: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("год високосный")
else:
    print("год не високосный")

#5
num = input("введите 5 значное число: ")
if num[0]==num[4] and num[1]== num[3]:
    print("ваше число палиндром")
else:
    print("число не палиндром")

#6
usd = float(input("введите количество USD: "))
currency = input("введите валюту (EUR, UAN, AZN, RUB): ").upper()
if currency == "EUR":
    print("сумма в EUR:", usd * 0.92)
elif currency == "UAN":
    print("сумма в UAN:", usd * 40.0)
elif currency == "AZN":
    print("сумма в AZN:", usd * 1.70)
elif currency == "RUB":
    print("сумма в RUB:", usd * 91.5)
else:
    print("введена неизвестная валюта")

#7
total = float(input("введите сумму: "))
if total < 200:
    print("скидки нет. К оплате", total)
elif 200 <= total < 300:
    print("скидка 3%. К оплате:", total * 0.97)
elif 300 <= total < 500:
    print("скидка 5%. К оплате:", total * 0.95)
else:
    print("скидка 7%. К оплате: ", total * 0.93)

#8
l_circle = float(input("введите длину окружносити: "))
p_square = float(input("введите периметр квадрата: "))
diameter = l_circle / 3.14
side = p_square / 4
if diameter <= side:
    print("окружность поместиться в квадрат")
else:
    print("окружность не поместиться в квадрат")

#9
scores = 0
print("сколько четвертей в баскетбольном матче?")
print("1) 1  2) 4  3) 7")
ans1 = input("ваш ответ: ")
if ans1 == "2":
    scores += 2
print("сколько очков дают за поподание изза дуговой зоны?")
print("1) 1  2) 5  3) 3")
ans2 = input("ваш ответ: ")
if ans2 == "3":
    scores += 2
print("какого размера баскетбольны мяч в лиге NBA?")
print("1) 7  2) 8  3) 9")
ans3 = input("ваш ответ: ")
if ans3 == "1":
    scores += 2
print("Опрос окончен! Вы набрали очков",scores)

#10
day = int(input("введите день: "))
month = int(input("введите месяц: "))
year = int(input("введите год: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    max_days = 31
elif month in [4, 6, 9, 11]:
    max_days = 30
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        max_days = 29
    else:
        max_days = 28
day += 1
if day > max_days:
    day = 1
    month += 1
if month > 12:
    month = 1
    year += 1
print("следующая дата:",day,".",month,".",year)
