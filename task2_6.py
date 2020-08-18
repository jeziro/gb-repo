n = 0
items = []
itemFeatures = {'name': '', 'price': '', 'quantity': '', 'measure': ''}
itemAnalytics = {'name': [], 'price': [], 'quantity': [], 'measure': []}
while True:
    s = input('Для добавления предмета введите add, если хотите закончить exit, аналитика - a').upper()
    if s == "ADD":
        n += 1
        for k in itemFeatures.keys():
            _ = input(f'Введите значение свойства "{k}": ')
            itemFeatures[k] = int(_) if (k == 'price' or k == 'quantity') else _
            itemAnalytics[k].append(itemFeatures[k])
            items.append((n, itemFeatures))
    elif s == 'EXIT':
        break
    else:
        for count, value in itemAnalytics.items():
            print(f'{count}: {value}')