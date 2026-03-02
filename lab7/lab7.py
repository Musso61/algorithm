# ЗАДАНИЕ 1. Функции и параметры
# ================================

def add(a, b):
    return a + b


def power(a, n=2):
    return a ** n


def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total


# ================================
# ЗАДАНИЕ 2. Область видимости
# ================================

global_var = 10  # глобальная переменная


def change_global():
    global global_var
    global_var += 5


print("Глобальная переменная до изменения:", global_var)
change_global()
print("Глобальная переменная после изменения:", global_var)

# Объяснение:
# Глобальная переменная объявляется вне функции и доступна во всей программе.
# Локальная переменная создаётся внутри функции и доступна только в ней.
# Чтобы изменить глобальную переменную внутри функции, используется ключевое слово global.


# ================================
# ЗАДАНИЕ 3. Рекурсивный факториал
# ================================

# Рекурсивная версия
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Итерационная версия
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print("Факториал (рекурсивно) 5:", factorial_recursive(5))
print("Факториал (итерационно) 5:", factorial_iterative(5))

# Сложность:
# Время: O(n)
# Память:
# - рекурсия O(n) (из-за стека вызовов)
# - итерация O(1)


# ================================
# ЗАДАНИЕ 4. Рекурсивная сумма цифр
# ================================

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


print("Сумма цифр 1234:", sum_digits(1234))


# ================================
# ЗАДАНИЕ 5. Рекурсивный максимум списка
# ================================

def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    sub_max = max_element(arr, index + 1)
    return arr[index] if arr[index] > sub_max else sub_max


print("Максимум списка:", max_element([3, 7, 2, 9, 5]))


# ================================
# ДОПОЛНИТЕЛЬНО: Фибоначчи
# ================================

# Обычная рекурсия
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Оптимизированная версия (мемоизация)
def fibonacci_fast(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_fast(n - 1, memo) + fibonacci_fast(n - 2, memo)
    return memo[n]


print("Фибоначчи (обычно) 6:", fibonacci(6))
print("Фибоначчи (быстро) 30:", fibonacci_fast(30))

# Сложность:
# Обычная рекурсия: O(2^n)
# Оптимизированная: O(n)


# =====================================
# ПРАКТИЧЕСКИЕ ЗАДАЧИ (базовый уровень)
# =====================================

def average(a, b, c):
    return (a + b + c) / 3


def is_even(n):
    return n % 2 == 0


def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)


print("Среднее:", average(3, 6, 9))
print("Чётное ли 4:", is_even(4))
print("Степень по умолчанию:", power(5))
print("Сумма всех чисел:", sum_all(1, 2, 3, 4, 5))
print("Вывод от 5 до 1:")
print_reverse(5)


# =====================================
# ПРАКТИЧЕСКИЕ ЗАДАЧИ (средний уровень)
# =====================================

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


print("Сумма цифр 245:", sum_digits(245))
print("Палиндром 'казак':", is_palindrome("казак"))
print("Максимум:", max_element([10, 3, 25, 7]))


# Быстрое возведение в степень
def fast_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half
    return a * fast_power(a, n - 1)


print("Быстрое возведение 2^10:", fast_power(2, 10))


# Подсчёт глубины рекурсии
def count_depth(n):
    if n == 0:
        return 1
    return 1 + count_depth(n - 1)


print("Глубина рекурсии для 5:", count_depth(5))

# Вывод:
# Глубина рекурсии линейно зависит от n → сложность O(n)