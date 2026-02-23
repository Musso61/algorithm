import random

# Задание 1
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

print("\nМатрица:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

total = 0
maximum = matrix[0][0]
for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма элементов:", total)
print("Максимальный элемент:", maximum)


# Задание 2
print("\n--- Задание 2 ---")
row_sums = []
for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Сумма строки {i}: {row_sum}")

for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Сумма столбца {j}: {col_sum}")

max_row_index = row_sums.index(max(row_sums))
print("Строка с максимальной суммой:", max_row_index)


# Задание 3
print("\n--- Задание 3 ---")
def shift_right(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row

game_matrix = [
    [0, 2, 0, 4],
    [1, 0, 3, 0],
    [0, 0, 5, 6],
    [7, 0, 0, 8]
]

print("До сдвига:")
for row in game_matrix:
    print(row)

for i in range(4):
    game_matrix[i] = shift_right(game_matrix[i])

print("\nПосле сдвига вправо:")
for row in game_matrix:
    print(row)