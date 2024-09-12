def my_func(a, b):
    if a == 0 or b == 0:
        print("Введите значение, отличное от нуля")
    else:
        c = a/b
        print(c)
while True: #добавил для удобной проверки всех значений
    my_func(int(input('Введите первое число')), int(input('Введите второе число')))


