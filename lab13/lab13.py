import time
import random

# =========================
# Замер времени
# =========================
def measure(func, *args):
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start


# =========================
# 1. Поиск
# =========================
def linear_search(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] == x:
            return True
        elif arr[m] < x:
            l = m+1
        else:
            r = m-1
    return False

def test_search():
    print("\n=== Поиск ===")
    sizes = [100, 1000, 10000, 100000]

    for n in sizes:
        arr = list(range(n))
        x = n-1

        t1 = measure(linear_search, arr, x)
        t2 = measure(binary_search, arr, x)

        print(f"n={n}: linear={t1:.6f}, binary={t2:.6f}")


# =========================
# 2. Сортировки
# =========================
def bubble_sort(a):
    a=a[:]
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

def insertion_sort(a):
    a=a[:]
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a

def selection_sort(a):
    a=a[:]
    for i in range(len(a)):
        m=i
        for j in range(i+1,len(a)):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]
    return a

def test_sorts():
    print("\n=== Сортировки O(n^2) ===")
    arr = [random.randint(0,1000) for _ in range(2000)]

    print("Bubble:", measure(bubble_sort, arr))
    print("Insertion:", measure(insertion_sort, arr))
    print("Selection:", measure(selection_sort, arr))


# =========================
# 3. QuickSort
# =========================
def quicksort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    left=[x for x in a[1:] if x<=pivot]
    right=[x for x in a[1:] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)

def test_quick():
    print("\n=== QuickSort ===")
    arr = [random.randint(0,10000) for _ in range(5000)]
    print("QuickSort:", measure(quicksort, arr))


# =========================
# 4. Сумма
# =========================
def sum_loop(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

def sum_formula(n):
    return n*(n+1)//2

def test_sum():
    print("\n=== Сумма ===")
    n=10_000_000
    print("Loop:", measure(sum_loop, n))
    print("Formula:", measure(sum_formula, n))


# =========================
# 5. Строки
# =========================
def slow_concat(n):
    s=""
    for _ in range(n):
        s+="a"
    return s

def fast_concat(n):
    return "".join(["a"]*n)

def test_strings():
    print("\n=== Строки ===")
    n=50000
    print("Slow:", measure(slow_concat, n))
    print("Fast:", measure(fast_concat, n))


# =========================
# 11. Фибоначчи
# =========================
def fib_rec(n):
    if n<=1:
        return n
    return fib_rec(n-1)+fib_rec(n-2)

def fib_iter(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def test_fib():
    print("\n=== Фибоначчи ===")
    print("Iter:", measure(fib_iter, 35))
    print("Rec (n=30):", measure(fib_rec, 30))


# =========================
# 12. Ханой
# =========================
def hanoi(n):
    if n==1:
        return 1
    return 2*hanoi(n-1)+1

# =========================
# 15. Merge
# =========================
def merge(a,b):
    i=j=0
    res=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


# =========================
# MAIN
# =========================
def main():
    test_search()
    test_sorts()
    test_quick()
    test_sum()
    test_strings()
    test_fib()

    print("\n=== Ханой ===")
    print("n=20:", hanoi(20))

    print("\n=== Merge ===")
    print(merge([1,3,5],[2,4,6]))

main()