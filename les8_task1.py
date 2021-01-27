import hashlib


def rk_sum(s: str, subs: str) -> int:
    assert len(s) >= len(subs), 'Подстрока длиннее строки'
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
    i = 0
    quan = 0
    while i < len(s) - len_sub + 1:
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if s[i:i + len_sub] == subs:
                quan += 1
                i += len_sub - 1
        i += 1
    return quan


def subs_quan(s):
    q = {}
    assert len(s) > 0, 'Строка не должна быть пустой'
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            q[s[i:j]] = rk_sum(s, s[i:j])
    return q


full_str = input('Введите строку: ')
q = subs_quan(full_str)
summ = {}
q.pop(full_str)
for k, v in q.items():
##    summ = int(summ + v) Неуспел доделать сумму, потому что забыл сделать сразу(
    print(f'Подстрока \'{k}\' встречается {v} раз(а)')
    print(f'Суммарное количество подстрок {summ}')