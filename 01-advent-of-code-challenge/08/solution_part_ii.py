from sys import stdin


tree_grid = []
max_score = 0


def get_direction_score(cur_tree: int, direction: "list[int]"):
    for d, tree in enumerate(direction, start=1):
        if tree < cur_tree: continue
        return d
    return len(direction)


for line in stdin:
    tree_grid.append(list(map(int, line.strip()[:])))


for i, row in enumerate(tree_grid[1:-1], start=1):
    for j, col in enumerate(row[1:-1], start=1):
        axis = [
            row[j-1::-1], # left (reversed)
            [u_row[j] for u_row in tree_grid[i-1::-1]], # top (reversed)
            row[j+1:], # right
            [d_row[j] for d_row in tree_grid[i+1:]], # bottom
        ]
        cur_score = 1
        for direction in axis:
            cur_score *= get_direction_score(col, direction)
        if cur_score > max_score: max_score = cur_score

print('Maior pontuação possível:', max_score)