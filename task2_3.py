my_list1 = ["зима", "весна", "осень", "лето"]
my_list2 = [[1, 2, 12], [3, 4, 5], [9, 10, 11], [6, 7, 8]]
dict_1 = {0: my_list1[0], 1: my_list1[1], 2: my_list1[2], 3: my_list1[3]}
n = int(input("Введите число месяца от 1 до 12"))
m = 0
p = 0
while n != p:
    for item in my_list2[m]:
        if n == int(item):
            print(dict_1.get(p))
            break
    if n != int(item):
        m += 1
        p += 1
    else:
        break
if n > 12:
    print(" Неподходящее значение. Введите число от 1 до 12")
