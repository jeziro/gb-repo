from collections import deque
from copy import deepcopy


def check16(lst):
    for idx, el in enumerate(lst):
        k = ord(el)
        if 48 > k or 57 < k < 65 or 70 < k < 97 or k > 102:
            print(f"{el} в {lst} не 16-ричный символ")
            return False
        lst[idx] = el.upper()
    return True

def ext_dim(n, m):
    if len(n) >= len(m):
        m = ['0' for _ in range(len(n) - len(m))] + m
    else:
        n = ['0' for _ in range(len(m) - len(n))] + n
    return n, m

def sum16_1(m, n):
    if len(m) > 1 or len(n) > 1:
        raise ValueError('Больше чем 1 символ')
    return sum16tab[t.index(m)][t.index(n)]


def sum16(m, n):
    res = deque()
    buff = '0'
    for i in range(-1, -len(m) - 1, -1):
        s = sum16_1(m[i], n[i])
        buff0 = buff
        if len(s) > 1:
            buff = s[0]
            s = sum16_1(s[1], buff0)

        else:
            s = sum16_1(s, buff0)
            buff = '0'
        if len(s) > 1:
            res.appendleft(s[1])
            buff = s[0]
        else:
            res.appendleft(s)
        if i == -len(m) and buff != '0':
            res.appendleft(buff)
    return list(res)


def mult16(m, n):
    s = ['1']
    one = ['1']
    res = m
    while s != n:
        s, n = ext_dim(deepcopy(s), deepcopy(n))
        s, one = ext_dim(deepcopy(s), deepcopy(one))
        s = sum16(s, one)
        res, m = ext_dim(deepcopy(res), deepcopy(m))
        res = sum16(res, m)
    return res


def gen16tab(t_deque):
    t_fix = list(t_deque)
    tab = [list(t_deque)]
    c = 1
    for i in t_fix[:-1]:
        t_deque.append(t_fix[c] + i)
        tab.append(list(t_deque))
    return tab


t = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'], maxlen=16)
sum16tab = gen16tab(deepcopy(t))

num1 = list(input("Введите 1е число,например F1B1 : "))
num2 = list(input("Введите 2е число,например A2C5 : "))
if check16(num1) and check16(num2):
    print(f'num1: {num1}')
    print(f'num2: {num2}')
    num1, num2 = ext_dim(deepcopy(num1), deepcopy(num2))

    print(f'Сумма: {sum16(num1, num2)}')
    print(f'Произведение: {mult16(num1, num2)}')