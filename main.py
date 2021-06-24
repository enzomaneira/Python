from itertools import combinations

obj = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in (3, len(obj)):
    for comb in combinations(obj, i):
        if sum(comb) == 12:
            v = comb[0]*3 + comb[1]*2 + comb[2]
            print(f'x = {comb[0]}  y = {comb[1]}  z = {comb[2]} | Valor = {v}\n')

print('N = 12')
