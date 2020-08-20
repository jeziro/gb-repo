surname = input('Введите фамилию')
name = input('Введите имя')
city = input('Введите город проживания')
year = input('Введите год рождения')
email = input('Введите email')
phone = input('Введите телефон')

def my_func(name, surname, year, city, email, phone):
    return ', '.join([name, surname, year, city, email, phone])

print(my_func(name, surname, year, city, email, phone))

