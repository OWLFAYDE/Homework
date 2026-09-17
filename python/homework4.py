a = int(input(" "))
b = int(input(" "))
total_sum = 0
for i in range(a,b+1):
    total_sum = total_sum + i
print(total_sum)

num1 = int(input(" "))
num2 = int(input(" "))
while num1 != num2:
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1
print(num1)

num = int(input(" "))
for i in range(1,num+1):
    if num % i == 0:
        print(i)

num = int(input(" "))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print(count)
