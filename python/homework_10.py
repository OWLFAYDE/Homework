#1-я функция: принимает строку и возвращает количество слов в строке

def count_words(text):
    words = text.split()
    return len(words)

print(count_words("hi your like pizza and roll ?"))

#2-я функция:  принимает строку и возвращает количество чисел в строке (именно чисел а не цифр)

def count_numbers(num):
    numbers = num.split()
    count = 0
    for i in numbers:
        if i.isdigit():
            count += 1

    return count
print(count_numbers("hi your want 2 pizza or 10 roll ?"))

#3-я функция: принимает строку и возвращает новую строку содержащую только повторяющиеся слова из первой строки

def duplicate_words(text):
    words = text.split()
    duplicated = []
    for i in words:
        if words.count(i) > 1 and i not in duplicated:
            duplicated.append(i)
    return " ".join(duplicated)

print(duplicate_words("hello world hello world"))
