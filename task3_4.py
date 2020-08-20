x = int(input('Введите положительное число'))
y = int(input('Введите целое отрицательное число'))

def my_func(x, y):
    while x >= 0 and y <= 0:
        if y == 0 or x == 0:
            print("1")
            break
        else:
            a = x**y
            print(a)
            break
    else:
        print("Введены неправильные данные")

my_func(x, y)
