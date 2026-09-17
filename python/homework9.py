list = [13,23,45,56,76,87,1,2,3,5,6,7,28,33,90,59]

# def bubble_sort(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-i-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]

# bubble_sort(list)
# print(list)

# def insertion_sort(list):
#     for i in range(1,len(list)):
#         key = list[i]
#         j = i-1
#         while j >= 0 and key < list[j]:
#             list[j+1] = list[j]
#             j -= 1
#         list[j + 1] = key

# insertion_sort(list)
# print(list)

# def shaker_sort(list):
#     left = 0
#     right = len(list)-1
#     while left <= right:
#         for i in range(left,right):
#             if list[i] > list[i + 1]:
#                 list[i],list[i+1] = list[i+1],list[i]
#         right -= 1

#         for i in range(right,left, - 1):
#             if list[i - 1] > list[i]:
#                 list[i - 1],list[i] = list[i],list[i - 1]
#         left += 1

# shaker_sort(list)
# print(list)

# def selection_sort(list):
#     for i in range(len(list)):
#         min_index = i
#         for j in range(i+1,len(list)):
#             if list[j] < list[min_index]:
#                 min_index = j
#         list[i],list[min_index] = list[min_index],list[i]
#
# selection_sort(list)
# print(list)
