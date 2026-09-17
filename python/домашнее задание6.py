import random

print("---Угадай число---")
player_score = 0
pc_score = 0
while True:
    cheat = 0
    summ = random.randint(1,99)
    while True:
        if cheat == 5:
            print(f"вы проиграли загаданное число: {summ}, попыток использовано: {cheat} ")
            pc_score += 1
            break
        pl = int(input("введите число: "))
        cheat += 1
        if pl == summ:
            print(f"Число угаданно:{summ}")
            player_score += 1
            break
        elif pl < summ:
            print("введеное число меньше загаданного")
        else:
            print("введеное число больше загаданного")
    again = input("Хотите сыграть еще?: ")
    if again == "no":
        break
print("----ОБЩАЯ СТАТИСТИКА----")
print(f"Игрок: {player_score} | Компьтер: {pc_score}")

