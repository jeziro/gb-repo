with open("text_3.txt", "r", encoding="utf-8") as my_f:
    summa = []
    less = []
    line = my_f.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        summa.append(i[1])
    average = sum(map(float, summa)) / len(summa)
print(f"Сотрудники, у которых зп меньше 20000 - {less}, Средняя зп - {average}")