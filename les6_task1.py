import sys

print(sys.version, sys.platform)

for k in range(15):
    num0 = 2 ** k
    print(f'Начальное число: {num0}')

    # Вариант 1
    num = num0
    num_rev = 0
    while num > 0:
        num_rev = 10 * num_rev + num % 10
        num //= 10

    print(f'Потребляемая память в варианте 1: {sys.getsizeof(num) + sys.getsizeof(num_rev)}')

    # Вариант 2
    num = num0
    num_list = []
    while num > 0:
        num_list.append((num % 10))
        num //= 10

    print(f'Потребляемая память в варианте 2: {sys.getsizeof(num) + sys.getsizeof(num_list)}')

    # Вариант 3
    num = num0
    s = str(num)
    s_r = ''
    for i in s[::-1]:
        s_r += i

    print(f'Потребляемая память в варианте 3: {sys.getsizeof(num) + sys.getsizeof(s) + sys.getsizeof(s_r)}')