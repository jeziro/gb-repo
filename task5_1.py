with open("text_1.txt", "w", encoding="utf-8") as my_f:
    while True:
        line = input("Введите текст. Чтобы закончить ввод нажмите Enter \n")
        my_f.write(line + "\n")
        if not line:
            break

with open("text_1.txt", "r", encoding="utf-8") as my_f:
    for i in my_f:
        print(i, end="")