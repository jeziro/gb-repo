rus = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
new_file = []
with open("text_4.txt", "r", encoding="utf-8") as my_f:
    content = my_f.read().split('\n')
    for i in content:
        i = i.split(" ", 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open("file_4_new.txt", "w", encoding="utf-8") as my_f:
    my_f.writelines(new_file)