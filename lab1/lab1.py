# 1)
# Линейный алгоритм

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

sum_result = a + b
diff_result = a - b
prod_result = a * b

print("Сумма:", sum_result)
print("Разность:", diff_result)
print("Произведение:", prod_result)

# 2)
# Алгоритм с ветвлением

x = int(input("Введите число: "))

if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# 3)
# Циклический алгоритм

n = int(input("Введите натуральное число n: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Сумма чисел от 1 до", n, "равна", total)