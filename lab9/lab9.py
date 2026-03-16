# Класс узла
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Класс связного списка
class LinkedList:
    def __init__(self):
        self.head = None

    # Добавление в начало
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Добавление в конец
    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Вывод списка
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Поиск элемента
    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    # Удаление первого элемента
    def delete_first(self):
        if self.head:
            self.head = self.head.next

    # Подсчет элементов
    def count(self):
        temp = self.head
        c = 0
        while temp:
            c += 1
            temp = temp.next
        return c

    # Разворот списка
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# ================================
# Основная программа (Задание 9)
# ================================

ll = LinkedList()

print("Введите 5 чисел:")

for i in range(5):
    num = int(input())
    ll.add_last(num)

print("Список:")
ll.print_list()

print("Количество элементов:", ll.count())

value = int(input("Введите число для поиска: "))
print("Найдено:" if ll.search(value) else "Не найдено")

print("Удаляем первый элемент...")
ll.delete_first()
ll.print_list()

print("Разворачиваем список...")
ll.reverse()
ll.print_list()
