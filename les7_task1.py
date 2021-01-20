import random
import copy


def bubble_desc(arr):
    n = 1
    while n < len(arr):
        k = 0
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                k += 1
        n += 1
    return arr


def bubble_desc_adv(arr):
    n = 1
    end_idx = len(arr)
    while n < end_idx:
        k = False
        for i in range(end_idx - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                k = True
        if not k:
            break
        n += 1
    return arr


lst = [random.randint(-100, 99) for _ in range(20)]

print(f'Начальный массив: {lst}')
lst_1 = bubble_desc(copy.deepcopy(lst))
print(f'Отсортированный массив: {lst_1}')
lst_2 = bubble_desc_adv(copy.deepcopy(lst))
print(f'Отсортированный массив улучшенный: {lst_2}')
print(f'Равны ли отсортированные массивы: {lst_1 == lst_2}')