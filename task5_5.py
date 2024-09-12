def summ():
    try:
        with open("text_5.txt", "w", encoding="utf-8") as my_f:
            line = input("Введите цифры через пробел \n")
            my_f.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Неправильно набран номер. Ошибка ввода-вывода")
summ()