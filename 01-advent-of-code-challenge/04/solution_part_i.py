from sys import stdin

ovrlaps = 0
for line in stdin:
    pair_a, pair_b = [tuple(map(int, v.split('-')))
                      for v in line.strip().split(',')]

    if pair_a[0] <= pair_b[0] and pair_a[1] >= pair_b[1]:
        ovrlaps += 1
    elif pair_b[0] <= pair_a[0] and pair_b[1] >= pair_a[1]:
        ovrlaps += 1

print(f'Zonas totalmente contidas no seu par: {ovrlaps}')
