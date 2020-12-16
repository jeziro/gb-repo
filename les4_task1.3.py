import timeit
import cProfile
import random

def count_list(s):
    init_list = [random.randint(0, 100) for _ in range(0, s)]
    ###print(f'Начальный массив: {init_list}')
    max_count_el = init_list[0]
    max_count = 1
    for el in init_list:
        curr_count = init_list.count(el)
        if curr_count > max_count:
            max_count_el = el
            max_count = curr_count
        ##elif max_count == curr_count and max_count >= 2:
        ##    print('Несколько элементов с одинаковым количеством повторений, попробуйте заново')

    ##print(f'Элемент {max_count_el} повторяется чаще остальных - {max_count}')

print(timeit.timeit('count_list(100)', number=100, globals=globals())) # 0.018117800000000003
print(timeit.timeit('count_list(200)', number=100, globals=globals())) # 0.05587299999999999
print(timeit.timeit('count_list(400)', number=100, globals=globals())) # 0.2009341
print(timeit.timeit('count_list(800)', number=100, globals=globals())) # 0.7830543000000001

cProfile.run('count_list(100)')  # 1    0.001    0.001    0.001    0.001 Les_4_task_1_v1.py:15(max_number)
                                 # 127    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('count_list(200)')  # 1    0.003    0.003    0.004    0.004 Les_4_task_1_v1.py:15(max_number)
                                 #  242    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('count_list(400)')  # 1    0.012    0.012    0.013    0.013 Les_4_task_1_v1.py:15(max_number)
                                 # 507    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('count_list(800)')  # 1    0.050    0.050    0.053    0.053 Les_4_task_1_v1.py:15(max_number)
                                 # 1016    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}