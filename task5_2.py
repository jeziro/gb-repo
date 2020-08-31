count = -1 #\n в прошлом файле добавляет пустую строку под конец, для правильного подсчета поставил -1
with open("text_1.txt", "r", encoding="utf-8") as my_f:
    for line in my_f:
        count += 1
        words_in_line = line.split()
        print(line, "Длинна строки - ", len(words_in_line))
    print("Всего строк в файле - ", count)

