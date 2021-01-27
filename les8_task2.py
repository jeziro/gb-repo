from collections import Counter
import heapq


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def expand(self, code, sym_start):
        if self.left:
            self.left.expand(code, sym_start + "0")
        if self.right:
            self.right.expand(code, sym_start + "1")
        if sym_start:
            code[self.data] = sym_start
        else:
            code[self.data] = '0'


def huff(phrase):
    phrase_count = Counter(phrase)
    hp = []
    for key, val in phrase_count.items():
        hp.append([val, len(hp), Node(data=key)])
    heapq.heapify(hp)
    t = len(hp)
    while len(hp) >= 2:
        el = heapq.heappop(hp)
        count1, symbol1 = el[0], el[2]
        el = heapq.heappop(hp)
        count2, symbol2 = el[0], el[2]
        heapq.heappush(hp, [count1 + count2, t, Node(left=symbol1, right=symbol2)])
        t += 1
    code = {}
    if hp:
        root_node = hp[0][2]
        root_node.expand(code, '')
    return code

in_phrase = input('Введите фразу: ')
codes = huff(in_phrase)
phrase_huff = ""
for s in in_phrase:
    phrase_huff += " ".join(codes[s])
print(f'Закодированная фраза: {phrase_huff}')
print('Коды каждого символа:')
for key, val in codes.items():
    if key:
        print(f'\'{key}\': {val}')