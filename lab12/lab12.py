# Задание 1
print("Задание 1")
students_grades = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 82,
    "Diana": 95,
    "Ethan": 88
}

for name, grade in students_grades.items():
    print(f"{name} – {grade}")

print("\n" + "-"*50 + "\n")

# Задание 2
print("Задание 2")
numbers = [5, 2, 5, 3, 2, 5]
count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(count_dict)

print("\n" + "-"*50 + "\n")

# Задание 3
print("Задание 3")
text = "algorithm"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

print("\n" + "-"*50 + "\n")

# Задание 4
print("Задание 4")
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012",
    "Diana": "456-789-0123",
    "Ethan": "567-890-1234"
}

search_name = "Charlie"
print(f"Номер {search_name}: {phone_book.get(search_name, 'Не найден')}")

print("\n" + "-"*50 + "\n")

# Задание 5
print("Задание 5")
words = ["cat", "dog", "cat", "bird", "dog", "dog"]
word_counts = {}
duplicates = []

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    if count > 1:
        duplicates.append(word)

print(duplicates)

print("\n" + "-"*50 + "\n")

# Задание 6
print("Задание 6")
str1 = "listen"
str2 = "silent"

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    count1 = {}
    count2 = {}
    for c in s1:
        count1[c] = count1.get(c, 0) + 1
    for c in s2:
        count2[c] = count2.get(c, 0) + 1
    return count1 == count2

print(f"Анаграммы: {are_anagrams(str1, str2)}")

print("\n" + "-"*50 + "\n")

# Задание 7
print("Задание 7")
products = {
    "apple": 50,
    "banana": 30,
    "orange": 40
}

# Добавление нового товара
products["grape"] = 60

# Изменение цены товара
products["banana"] = 35

# Удаление товара
del products["orange"]

# Поиск цены
search_product = "apple"
print(f"Цена {search_product}: {products.get(search_product, 'Не найден')}")

print("\n" + "-"*50 + "\n")

# Задание 8
print("Задание 8")
numbers_list = [4, 7, 1, 9, 7, 3, 1]
seen = set()
first_repeat = None

for num in numbers_list:
    if num in seen:
        first_repeat = num
        break
    seen.add(num)

print(f"Первое повторяющееся число: {first_repeat}")

print("\n" + "-"*50 + "\n")

# Задание 9
print("Задание 9")
text = "python is great and python is easy"
words = text.lower().split()
word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

most_common_word = max(word_freq, key=word_freq.get)
print(f"Слово, которое встречается чаще всего: {most_common_word}")

print("\n" + "-"*50 + "\n")

# Задание 10
print("Задание 10")
size = 10
hash_table = [[] for _ in range(size)]
numbers_to_insert = [15, 25, 35, 5, 20, 30]

for num in numbers_to_insert:
    index = num % size
    hash_table[index].append(num)

print("Содержимое хеш-таблицы:")
for i, bucket in enumerate(hash_table):
    print(f"{i}: {bucket}")

print("\n" + "-"*50 + "\n")