for i in range(2, 10):
    s = 0
    for j in range(2, 100):
        if j % i == 0:
            s += 1
    print(f'{i}: {s}')