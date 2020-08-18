a = input("Введите предложение")
i = 0
for word in a.split():
    i += 1
    print(i, word[:10])
