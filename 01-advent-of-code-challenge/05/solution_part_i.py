from sys import stdin


def get_crate_piles(buffer):
    piles = []
    for i, char in enumerate(pile_numbers_string):
        if char == ' ': continue
        piles.append([])

        for level in buffer[::-1]:
            if len(level) <= i or level[i] == ' ': continue
            piles[-1].append(level[i])

    return piles


def move_crates(amount, source, target):
    crate_piles[target] += crate_piles[source][-1:-amount-1:-1]
    crate_piles[source] = crate_piles[source][:-amount]


piles_buffer = []
for line in stdin:
    piles_buffer.append(line.rstrip())
    if not '[' in line: break
stdin.readline()

pile_numbers_string = piles_buffer.pop()
crate_piles = get_crate_piles(piles_buffer)

for line in stdin:
    X, Y, Z = map(int, line.split()[1::2])
    move_crates(X, Y-1, Z-1)

print('Caixas no topo das pilhas:', ''.join([pile[-1] for pile in crate_piles]))