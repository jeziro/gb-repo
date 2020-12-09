import random

init_list = []
idx = []
for i in range(0, 10):
    num = random.randint(1, 100)
    init_list.append(num)
    if num % 2 == 0:
        idx.append(i)

print(f'Первый массив: {init_list}')
print(f'Второй массив: {idx}')