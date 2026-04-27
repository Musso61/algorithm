from collections import Counter

# =========================
# Задача 1: Найти дубликаты
# =========================
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for x in arr:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    return list(duplicates)


# =========================
# Задача 2: Самое частое число
# =========================
def most_frequent(arr):
    count = Counter(arr)
    return count.most_common(1)[0][0]


# =========================
# Задача 3: Пара с суммой
# =========================
def find_pair(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return (target - num, num)
        seen.add(num)
    return None


# =========================
# Задача 4: Сортировка строк по длине
# =========================
def sort_by_length(strings):
    return sorted(strings, key=len)


# =========================
# Задача 5: Топ-3 слова
# =========================
def top_3_words(text):
    words = text.lower().split()
    count = Counter(words)
    return count.most_common(3)


# =========================
# Задача 6: Удалить дубликаты (с порядком)
# =========================
def remove_duplicates(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# =========================
# Задача 7: Пересечение списков
# =========================
def intersection(a, b):
    return list(set(a) & set(b))


# =========================
# Задача 8: Максимальный студент
# =========================
def best_student(students):
    return max(students, key=lambda x: x[1])


# =========================
# Задача 9: Чётные и нечётные
# =========================
def split_even_odd(arr):
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]
    return even, odd


# =========================
# Задача 10: Самая длинная последовательность
# =========================
def longest_sequence(arr):
    max_len = 1
    current = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            current += 1
            max_len = max(max_len, current)
        else:
            current = 1

    return max_len


# =========================
# Задача 11: Мини-система пользователей
# =========================
class UserSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, name, age):
        self.users[name] = age

    def find_user(self, name):
        return self.users.get(name, "Не найден")

    def delete_user(self, name):
        if name in self.users:
            del self.users[name]


# =========================
# ТЕСТЫ (чтобы показать результат)
# =========================
def main():
    print("1:", find_duplicates([1,2,2,3,4,4]))
    print("2:", most_frequent([1,1,2,3,3,3]))
    print("3:", find_pair([2,7,11,15], 9))
    print("4:", sort_by_length(["hi","hello","a"]))
    print("5:", top_3_words("hi hi hello hello hello test test"))
    print("6:", remove_duplicates([1,2,2,3,1,4]))
    print("7:", intersection([1,2,3],[2,3,4]))
    print("8:", best_student([("A",80),("B",95),("C",70)]))
    print("9:", split_even_odd([1,2,3,4,5,6]))
    print("10:", longest_sequence([1,1,1,2,2,3,3,3,3]))

    system = UserSystem()
    system.add_user("Ali", 20)
    system.add_user("Dana", 22)
    print("11:", system.find_user("Ali"))
    system.delete_user("Ali")
    print("11 после удаления:", system.find_user("Ali"))

main()