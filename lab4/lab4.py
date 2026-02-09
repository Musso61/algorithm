#первое задание

x = int(input("Введите целое число: "))

while x <= 0:
    x = int(input("Число должно быть положительным. Повторите ввод: "))

print("Корректное число:", x)


#второе задание

while True:
    x = int(input("Введите число: "))
    if x > 100:
        break

print("Введено число больше 100:", x)

#третье задание

n = int(input("Введите n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Сумма чисел от 1 до", n, "равна", total)

# четвертое задание

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()