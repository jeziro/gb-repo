my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list1 = [el for n, el in enumerate(my_list) if my_list[n - 1] < my_list[n]]
print(f'Исходный список {my_list}')
print(f'Итоговый список {my_list1}')