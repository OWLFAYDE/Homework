import random
# 1
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# mx = a
# if b > mx:
#     mx = b
# if c > mx:
#     mx = c
# if d > mx:
#     mx = d
# print(mx)

#2
# a = int(input("num a: "))
# b = int(input("num b: "))
# start = max(a, b)
# end = min(a, b)
# for i in range(start, end -1, -1):
#     print(i, end=" ")

#3
# n = int(input("storona kwadrata: "))
# num = 5
# for i in range(n):
#     for j in range(n):
#         print(num,end="\t")
#         num += 1
#     print()

#4
# ch = input(": ")
# if len(ch)==1 and 'A'<= ch <= 'Z':
#     print("yes")
# else: print("no")

#5
# lst = []
# num = 0
# for i in range(8):
#     lst.append(num)
#     num += 3
# print(lst)

#6
# rows = int(input("rows: "))
# cols = int(input("cols: "))
# a = int(input("a =  "))
# b = int(input("b =  "))
# left = min(a,b)
# right = max(a,b)
# matrix = []
# summa = 0
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         x = random.randint(left,right)
#         row.append(x)
#         summa += x
#
#     matrix.append(row)
# print(matrix)
# for row in matrix:
#     print(row)
# avg = summa / (rows * cols)
# print(avg)

#7
# lst = []
# num = 0
# for i in range(8):
#     lst.append(num)
#     num += 3
# mn = lst[0]
# mx = lst[0]
# for x in lst:
#     if x < mn:
#         mn = x
#     if x > mx:
#         mx = x
# print("min is ", mn)
# print("max is ", mx)

#8
# def find_number(lst, value):
#     for x in lst:
#         if x == value:
#             return True
#     return False
# numbers = [1,2,4,5,3,5,7]
# print(find_number(numbers, 3))
# print(find_number(numbers, 10))

#9
# def odd_numbers(list):
#     result = []
#     for i in list:
#         if i % 2 != 0:
#             result.append(i)
#     return result
# numbers = [1,23,34,46,1,2,44,6,15]
# print(odd_numbers(numbers))

#10
# def get_column(matrix, col):
#     result = []
#     for row in matrix:
#         result.append(row[col])
#     return result
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(get_column(matrix, 1))

#11
# def get_numbers(text):
#     numbers = []
#     num = ""
#     for char in text:
#         if char.isdigit():
#             num += char
#         else:
#             if num != "":
#                 numbers.append(num)
#                 num = ""
#     if num != "":
#         numbers.append(num)
#     return numbers
# str = input()
# numbers = get_numbers(str)

#12