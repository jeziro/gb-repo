s = int(input("Введите секунды"))
h = s//3600
m = s//60
if m > 59:
    m = m % 60
if s > 59:
     s = s % 60
print(f"{h:02}:{m:02}:{s:02}")
