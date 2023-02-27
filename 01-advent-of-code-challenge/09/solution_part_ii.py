from sys import stdin

knots = 10
knots_pos = [[0, 0] for _ in range(knots)]
t_upos = {(0, 0)}


def calc_pos(prev_knot, next_knot):
    deltas = {
        (0, 2): (0, 1),
        (1, 2): (1, 1),
        (2, 2): (1, 1),
        (2, 1): (1, 1),
        (2, 0): (1, 0),
        (2, -1): (1, -1),
        (2, -2): (1, -1),
        (1, -2): (1, -1),
        (0, -2): (0, -1),
        (-1, -2): (-1, -1),
        (-2, -2): (-1, -1),
        (-2, -1): (-1, -1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-2, 2): (-1, 1),
        (-1, 2): (-1, 1),
    }
    delta = deltas.get((prev_knot[0] - next_knot[0], prev_knot[1] - next_knot[1]), (0, 0))
    return [next_knot[0] + delta[0], next_knot[1] + delta[1]]


for line in stdin:
    side, n = line.split()
    n = int(n)
    for _ in range(n):
        knots_pos[0][int(side in 'UD')] += 1 if side in 'RU' else -1
        for i in range(1, knots):
            t = knots_pos[i]
            knots_pos[i] = calc_pos(knots_pos[i-1], knots_pos[i])
            if knots_pos[i] == t:
                break
        t_upos.add(tuple(knots_pos[-1]))

print(f'Quantidade de posições únicas da cauda: {len(t_upos)}')