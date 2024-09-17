from math import factorial
from itertools import count

def gen():
    for el in count(1):
        yield factorial(el)

n = int(input('Введите число для вычисления факториала'))

num = gen()
a = 0
for i in num:
    if a < n:
        print(i)
        a += 1
    else:
        break
        