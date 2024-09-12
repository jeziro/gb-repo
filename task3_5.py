def my_sum ():
    sum_a = 0
    exit = []
    while exit != 'Q':
        numbers = input('Введите числа или q для выхода').upper().split()
        a = 0
        for b in range(len(numbers)):
            if numbers[b] == 'Q':  #оставил, чтобы ошибку перевода в инт не выдавало при вводе q
                break
            else:
                a = a + int(numbers[b])
        sum_a = sum_a + a
        print(f'Промежуточная сумма равна {sum_a}')
    print(f'Итоговая сумма равна {sum_a}')


my_sum()