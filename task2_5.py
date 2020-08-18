my_list = [7, 5, 3, 3, 2]
while len(my_list) < 10:
    print(my_list)
    a = int(input("Введите новый элемент"))
    for num in my_list:
        if a == num:
            my_list.insert(my_list.index(num), a)
            print(my_list)
            break
        else:
            my_list.append(a)
            my_list.sort()
            my_list.reverse()
            print(my_list)
            break
