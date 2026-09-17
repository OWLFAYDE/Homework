#1
material_type = input("введите тип убеного материала(книга/видео): ")
price = float(input("введите стоимость материала: "))
if price <= 0:
    print("ошибка: вы ввели отрицательное число")
else:
    category = input("введите категорию материала: ")
    print(f"материал добавлен: Тип - {material_type}, стоимость - {price}, категория - {category}")

