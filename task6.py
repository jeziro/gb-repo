a = int(input("Введите результат первого дня"))
b = int(input("Введите требуемый результат"))
dayCount = 1
while a < b:
    a = a + a/100 * 10
    dayCount += 1
    print(f"В {dayCount} день пройдено {a:.02f} километров")
    if a >= b:
        print(f"Номер дня требуемого результата: {dayCount}" )

