with open("text_6.txt", "r", encoding="utf-8") as my_f:
    subj = my_f.readlines()
    for line in subj:
        new1 = "".join((i if i in "1234567890" else "") for i in line)
        new2 = [int(i) for i in new1.split()]
        print(f"Общее количество часов по предмету {line.split()[0]} {sum(new2)}")