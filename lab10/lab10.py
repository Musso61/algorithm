# Задача 1: Класс Node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Задача 2: Создание бинарного дерева с заданными значениями
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)

print("Задача 2: Дерево")
print(f"Корень: {root.value}")
print(f"Левый потомок: {root.left.value}")
print(f"Правый потомок: {root.right.value}")

# Задача 3: Preorder (узел → левое → правое)
def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

print("\nЗадача 3: Preorder обход")
preorder(root)
print()

# Задача 4: Inorder (левое → узел → правое)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

print("\nЗадача 4: Inorder обход")
inorder(root)
print()

# Задача 5: Postorder (левое → правое → узел)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

print("\nЗадача 5: Postorder обход")
postorder(root)
print()

# Задача 6: Подсчёт количества узлов
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

print("\nЗадача 6: Количество узлов")
print(count_nodes(root))

# Задача 7: Определение высоты дерева
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print("\nЗадача 7: Высота дерева")
print(tree_height(root))

# Задача 8: Подсчёт количества листьев
def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

print("\nЗадача 8: Количество листьев")
print(count_leaves(root))

# Задача 9: Поиск значения в дереве
def search_tree(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    return search_tree(node.left, value) or search_tree(node.right, value)

search_val = 25
print(f"\nЗадача 9: Поиск {search_val}")
print(search_tree(root, search_val))

search_val = 40
print(f"Поиск {search_val}")
print(search_tree(root, search_val))

# Задача 10: Полная программа с обходами и статистикой
print("\nЗадача 10: Полная программа")
print("Preorder: ", end='')
preorder(root)
print("\nInorder: ", end='')
inorder(root)
print("\nPostorder: ", end='')
postorder(root)
print(f"\nКоличество узлов: {count_nodes(root)}")
print(f"Количество листьев: {count_leaves(root)}")
print(f"Высота дерева: {tree_height(root)}")

# Дополнительное задание: Вставка нового элемента в бинарное дерево поиска
def insert_bst(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert_bst(node.left, value)
    elif value > node.value:
        node.right = insert_bst(node.right, value)
    return node

# Пример вставки
root = insert_bst(root, 12)
root = insert_bst(root, 28)

print("\nПосле вставки новых элементов (12 и 28):")
print("Inorder обход: ", end='')
inorder(root)
print()
print(f"Количество узлов: {count_nodes(root)}")
print(f"Количество листьев: {count_leaves(root)}")
print(f"Высота дерева: {tree_height(root)}")