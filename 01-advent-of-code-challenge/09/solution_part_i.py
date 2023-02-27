from sys import stdin


h_pos = [0, 0]
t_pos = [0, 0]
t_upos = {(0, 0)}


def calc_pos(side: str):
    axis = int(side in 'UD')
    o_axis = 1 - axis
    delta = 1 if side in 'RU' else -1

    h_pos[axis] += delta
    if abs(h_pos[axis] - t_pos[axis]) > 1:
        t_pos[axis] += delta
        t_pos[o_axis] += h_pos[o_axis] - t_pos[o_axis]
        t_upos.add(tuple(t_pos))


for line in stdin:
    side, n = line.split()
    n = int(n)
    for _ in range(n):
        calc_pos(side)

print(f'Quantidade de posições únicas da cauda: {len(t_upos)}')