def my_func(a, b, c):
    sum1 = []
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    sum1 = sum(my_list)
    return sum1


print(f'Result - {my_func(int(input("Введите первое число")), int(input("Введите второе число")), int(input("Введите третье число")))}')