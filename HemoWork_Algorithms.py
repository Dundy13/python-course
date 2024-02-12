#Сортиране - Bubble Sort: Имплементирайте алгоритъм за Bubble Sort и тествайте със списък от цели числа.
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for h in range(0, n-i-1):

            if arr[h] > arr[h+1]:
                arr[h], arr[h+1] = arr[h+1], arr[h]

example_list = [85, 63, 18, 26, 31, 12, 13, 48]

print(example_list)

bubble_sort(example_list)

print(example_list)


#Selection Sort: Имплементирайте алгоритъма за сортиране Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        mid_index = i

        for h in range(i+1, n):
            if arr[h] < arr[mid_index]:
                mid_index = h


        arr[i], arr[mid_index] = arr[mid_index], arr[i]


example_list = [64, 28, 22, 11, 12, 9, 90]
print(example_list)

selection_sort(example_list)
print(example_list)



#Insertion Sort: Създайте функция, която използва алгоритъма Insertion Sort за сортиране на масив от числа.
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        h = i - 1
# Преместваме на елементи наляво от текущия индекс, които са по-големи от key
        while h >=0 and key < arr[h]:
            arr[h + 1] = arr[h]
            h -= 1

        arr[h +1] = key

example_list = [12, 85, 42, 17, 32, 54, 56]
print(example_list)

insertion_sort(example_list)
print(example_list)



# Binary search. Имлементирайте Binary search алгоритъм за намиране дали дадено число съществува в даден лист. За целта си
# създайте масив от 100 елемента със случайни числа и друго случайно число, което да търсите в масива.

import random

def binary_search(arr, target):
    arr.sort()

    left, right = 0, len(arr) -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False

random_numbers = [random.randint(1, 1000) for _ in range(100)]

search_target = random.choice(random_numbers)

print(random_numbers)
print(search_target)

if binary_search(random_numbers, search_target):
    print(f"Числото {search_target} е намерено в масива.")
else:
    print(f"Числото {search_target} не е намерено в масива.")