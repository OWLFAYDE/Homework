
matrix = [
    [2, 3, 4, 5],
    [2, 4, 3, 5],
    [4, 3, 4, 2]
]

n = len(matrix)  # Количество строк
m = len(matrix[0])  # Количество столбцов


def get_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total


def get_average(arr):
    return get_sum(arr) / len(arr)


def get_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum


def get_max_index(arr):
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx


def get_min(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum


def get_min_index(arr):
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def get_matrix_sum(mat):
    total = 0
    for row in mat:
        total += get_sum(row)
    return total


def get_matrix_average(mat):
    total_elements = len(mat) * len(mat[0])
    return get_matrix_sum(mat) / total_elements


def get_matrix_max_with_index(mat):
    max_val = mat[0][0]
    max_row, max_col = 0, 0
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] > max_val:
                max_val = mat[r][c]
                max_row, max_col = r, c
    return max_val, max_row, max_col


def get_matrix_min_with_index(mat):
    min_val = mat[0][0]
    min_row, min_col = 0, 0
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] < min_val:
                min_val = mat[r][c]
                min_row, min_col = r, c
    return min_val, min_row, min_col

print("=== РАСЧЕТ ДЛЯ СТРОК ===")
for i in range(n):
    row = matrix[i]
    print(f"Строка {i}:")
    print(f"Сумма: {get_sum(row)}")
    print(f"Среднее: {get_average(row)}")
    print(f"Максимум: {get_max(row)} (индекс {get_max_index(row)})")
    print(f"Минимум: {get_min(row)} (индекс {get_min_index(row)})")

print("\n=== РАСЧЕТ ДЛЯ СТОЛБЦОВ ===")
for j in range(m):
    column = []
    for i in range(n):
        column.append(matrix[i][j])

    print(f"Столбец {j}:")
    print(f"Сумма: {get_sum(column)}")
    print(f"Среднее: {get_average(column)}")
    print(f"Максимум: {get_max(column)} (индекс {get_max_index(column)})")
    print(f"Минимум: {get_min(column)} (индекс {get_min_index(column)})")

print("\n=== РАСЧЕТ ДЛЯ ВСЕЙ ТАБЛИЦЫ ===")
mx_val, mx_r, mx_c = get_matrix_max_with_index(matrix)
mn_val, mn_r, mn_c = get_matrix_min_with_index(matrix)

print(f"Общая сумма: {get_matrix_sum(matrix)}")
print(f"Общее среднее: {get_matrix_average(matrix)}")
print(f"Максимум в таблице: {mx_val} (строка {mx_r}, столбец {mx_c})")
print(f"Минимум в таблице: {mn_val} (строка {mn_r}, столбец {mn_c})")
