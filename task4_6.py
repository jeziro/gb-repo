from itertools import count

for el in count(int(input('Введите стартовое число '))):
   if el > 100:
       break
   print(el)


from itertools import cycle

my_list = [True, 'ABC', 123, None]
count = 0
for el in cycle(my_list):
    if count > 10:
        break
    print(el)
    count += 1
