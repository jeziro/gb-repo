import random


init_list = [random.randint(-5, 20) for _ in range(0, 10)]
print(f'Начальный массив: {init_list}')

max_negative = 0
neg_idx = 0
flag = True
for idx in range(0, len(init_list)):
    if init_list[idx] < 0:
        if flag:
            max_negative = init_list[idx]
            neg_idx = idx
            flag = False
        if init_list[idx] > max_negative:
            max_negative = init_list[idx]
            neg_idx = idx
if max_negative == 0:
    print("Отрицательные элементы не найдены")
else:
    print(f'Максимальный отрицательный элемент {max_negative} с индексом {neg_idx}')